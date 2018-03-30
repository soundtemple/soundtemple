from django.apps import apps
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView

from .forms import CommentForm
from .models import Comment

decorators = [login_required, staff_member_required]


@method_decorator(login_required, name='dispatch')
class AddPostComment(CreateView):

    model = Comment
    fields = ['text']
    template_name = 'comments/comment_add.html'

    def get(self, request, pk, *args, **kwargs):
        form = CommentForm(initial={'user': request.user})
        Post = apps.get_model('blog', 'Post')
        post = get_object_or_404(Post, pk=pk)

        context = {}
        context.update({
            'form': form,
            'post': post,
            'comment_type': Comment.COMMENT_TYPES[0][1],
        })

        return render(request, self.template_name, context)

    def post(self, request, pk):
        Post = apps.get_model('blog', 'Post')
        post = get_object_or_404(Post, pk=pk)

        form = CommentForm(request.POST)
        form.instance.user = self.request.user

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.category = Comment.COMMENT_TYPES[0][0]
            comment.save()
            return redirect('article-detail', pk=pk)


@staff_member_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    next_page = request.GET['next']
    return HttpResponseRedirect(next_page)


@staff_member_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    next_page = request.GET['next']
    return HttpResponseRedirect(next_page)





