from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 4

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')






