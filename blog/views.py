from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Comment, Post, Tag
from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CommentForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


decorators = [login_required, staff_member_required]

# Create your views here.


@method_decorator(decorators, name='dispatch')
class ArticleCreateView(CreateView):

    model = Post
    fields = ['title', 'subtitle', 'body', 'tags']
    template_name = 'blog/article_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['tags'] = Tag.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(decorators, name='dispatch')
class ArticleUpdateView(UpdateView):
    model = Post
    fields = ['title', 'subtitle', 'body', 'tags']
    template_name = 'blog/article_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['tags'] = Tag.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(decorators, name='dispatch')
class ArticleDeleteView(DeleteView):
    model = Post
    template_name = 'blog/article_delete.html'
    success_url = reverse_lazy('article-list')


class ArticleListView(ListView):

    model = Post
    template_name = 'blog/article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['tags'] = Tag.objects.all()
        if hasattr(self, 'tag'):
            context['filtered_by'] = self.tag.title
        return context


class TaggedArticleListView(ArticleListView):
    '''
    Filter Article list by tag
    '''

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, title=self.kwargs['tag'])
        return Post.objects.filter(tags=self.tag)


class ArticleDetailView(DetailView):

    model = Post
    template_name = 'blog/article_detail.html'
    form = CommentForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


@method_decorator(login_required, name='dispatch')
class AddCommentToPost(CreateView):

    def get(self, request, pk):
        form = CommentForm(initial={'user':request.user})
        post = get_object_or_404(Post, pk=pk)
        context = {'form': form, 'post': post}

        return render(request, 'blog/comment_add.html', context=context)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        form = CommentForm(request.POST)
        form.instance.user = self.request.user

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('article-detail', pk=post.pk)



@staff_member_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('article-detail', pk=comment.post.pk)


@staff_member_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('article-detail', pk=comment.post.pk)
