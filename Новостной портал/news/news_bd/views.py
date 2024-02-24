from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-time_post'
    context_object_name = 'posts'
    template_name = 'news.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'concrete_news.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'
