from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from Insta.models import Post, InstaUser
from Insta.forms import CustomUserCreationForm

# Create your views here.
class HelloDjango(TemplateView):
    template_name = 'home.html'

class PostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts.html'
    login_url = 'login'

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "make_post.html"
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ('title',)

class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('post')
  

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')
