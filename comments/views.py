from django.apps import apps
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView

from .forms import CommentForm
from .models import Comment

decorators = [login_required, staff_member_required]


class CommentMixin(object):
    model = Comment

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Comment'})
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CommentMixin, self).dispatch(*args, **kwargs)


@method_decorator(login_required, name='dispatch')
class AddComment(CreateView):

    model = Comment
    fields = ['text']
    template_name = 'comments/comment_add.html'

    def get(self, request, *args, **kwargs):
        form = CommentForm(initial={'user': request.user})
        context = {}
        context.update({
            'form': form,
        })

        if 'post_id' in request.GET:
            Post = apps.get_model('blog', 'Post')
            post = get_object_or_404(Post, pk=request.GET['post_id'])
            context.update({
                'post': post,
                'comment_type': Comment.COMMENT_TYPES[0][1],
            })
        if 'type' in request.GET and request.GET['type'] == 'testimonial':
            context.update({
                'comment_type': Comment.COMMENT_TYPES[3][1],
            })
        else:
            raise Http404

        return render(request, self.template_name, context)

    def post(self, request):

        form = CommentForm(request.POST)
        form.instance.user = self.request.user

        if form.is_valid():
            comment = form.save(commit=False)
            if 'post_id' in request.GET:
                # Handle news article post comment
                Post = apps.get_model('blog', 'Post')
                post = get_object_or_404(Post, pk=request.GET['post_id'])
                comment.post = post
                comment.category = Comment.COMMENT_TYPES[0][0]
                comment.save()
                return redirect('article-detail', pk=request.GET['post_id'])

            if 'type' in request.GET and request.GET['type'] == 'testimonial':
                # Handle testimonial submission
                comment.category = Comment.COMMENT_TYPES[3][0]
                comment.save()
                return redirect(request.GET['next'])
            else:
                return Http404


@method_decorator(decorators, name='dispatch')
class CommentDelete(CommentMixin, DeleteView):
    template_name = 'comments/comment_confirm_delete.html'

    def get_success_url(self):

        obj_to_delete = self.get_object()

        if 'path' in self.request.GET and self.request.GET['path'] == 'list':
            return reverse('comment-list')

        if obj_to_delete.category == Comment.COMMENT_TYPES[0][0]:
            # Delete News POST article
            return reverse('article-detail', args=(obj_to_delete.post.id,))

        else:
            return reverse('home_page')


@staff_member_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()

    if 'path' in request.GET and request.GET['path'] == 'list':
        return HttpResponseRedirect(reverse('comment-list'))

    if comment.category == Comment.COMMENT_TYPES[0][0]:
        # Approve News POST article
        return HttpResponseRedirect(reverse('article-detail', args=(comment.post.id,)))
    else:
        return HttpResponseRedirect(reverse('home_page'))


@method_decorator(decorators, name='dispatch')
class CommentsListView(ListView):

    model = Comment
    template_name = 'comments/comment_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class TestimonialList(ListView):
    model = Comment
    template_name = 'comments/testimonial_list.html'
    ordering = ['-featured',  '-created_on']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['testimonials'] = Comment.objects.filter(category=Comment.COMMENT_TYPES[3][0])\
                                .exclude(approved_comment=False).order_by('-featured', '-created_on')
        return context


@staff_member_required
def comment_feature_toggle(request, pk, feature):
    comment = get_object_or_404(Comment, pk=pk)
    if feature == 'True':
        comment.featured = True
        comment.feature()
    elif feature == 'False':
        comment.featured = False
        comment.unfeature()
    else:
        pass

    if 'path' in request.GET and request.GET['path'] == 'list':
        return HttpResponseRedirect(reverse('comment-list'))
    else:
        return HttpResponseRedirect(reverse('home_page'))