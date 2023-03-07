from django.shortcuts import render
from django.views import generic
from mypost.models import Post
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from mypost.forms import PostForm

class IndexView(generic.ListView):
    template_name = 'mypost/index.html'
    context_object_name = 'latest_post_list'
    def get_queryset(self):
        return Post.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Post
    template_name = 'mypost/detail.html'

class PostListView(generic.ListView):
    template_name = 'mypost/all.html'
    context_object_name = 'all_post_list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')

class PostCreateView(CreateView):
    # model = Post
    form_class = PostForm
    context_object_name = 'post_create'
    template_name = 'mypost/post_create.html'
    success_url = reverse_lazy('mypost:index')

class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'post_delete'
    success_url = reverse_lazy('mypost:index')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class PostUpdateView(UpdateView):
    # model = Post
    form_class = PostForm
    context_object_name = 'post_update'
    template_name = 'mypost/post_update.html'
    success_url = reverse_lazy('mypost:index')