from django.apps import apps
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Post, Tag

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

    def get_context_data(self, **kwargs):
        comments_model = apps.get_model('comments', 'Comment')
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['comments'] = comments_model.objects.filter(category=comments_model.COMMENT_TYPES[0][0], post=context['post'].pk)
        return context

