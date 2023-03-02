from django.views.generic import ListView, DetailView, CreateView

from .models import *


# Create your views here.


class PostList(ListView):
    model = Post  # use in the template default [ object_list or post_list ]
    context_object_name = 'posts'
    ordering = ['-created_at']
    # queryset = Post.objects.filter(active=True)
    template_name = 'post/index.html'

    def get_queryset(self):
        return Post.objects.filter(active=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = True
        return context


class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    pass
