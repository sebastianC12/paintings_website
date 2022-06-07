from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html')



class PostDetailView(DetailView):
    model = Post
    template_name = "main/post_details.html"

class PostCreate(CreateView):
    model = Post
    template_name = "main/post_create_form.html"
    fields = ['title', 'type', 'price', 'image']

class PostUpdate(UpdateView):
    model = Post
    template_name = "main/post_update_form.html"
    fields = ['title', 'type', 'price', 'image']

class PostDelete(DeleteView):
    model = Post
    template_name = "main/post_delete_form.html"
    success_url = '/home'

