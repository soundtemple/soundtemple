from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Comment, Post, Tag
from django.utils import timezone
from django.urls import reverse_lazy

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
        return context


class ArticleDetailView(DetailView):

    model = Post
    template_name = 'blog/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


