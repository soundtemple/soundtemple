from django import template
from django.apps import apps

register = template.Library()


@register.inclusion_tag('comments/widget_testimonials.html')
def footer_testimonials():
    Comment = apps.get_model('comments', 'Comment')
    featured_testimonials = Comment.objects.filter(featured=True)[:5]

    return {'featured_testimonials': featured_testimonials}


@register.inclusion_tag('comments/widget_news.html')
def footer_news():
    Post = apps.get_model('blog', 'Post')
    featured_posts = Post.objects.order_by('-published')[:5]
    return {'featured_posts': featured_posts}