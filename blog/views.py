from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Comment, Post, Tag
from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CommentForm

# Create your views here.


class ArticleCreateView(CreateView):

    model = Post
    fields = ['title', 'body', 'author', 'tags']
    template_name = 'blog/article_create.html'


class ArticleUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body', 'author', 'tags']
    template_name = 'blog/article_edit.html'


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('article-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_add.html', {'form': form})


def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('article-detail', pk=comment.post.pk)


def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('article-detail', pk=comment.post.pk)
