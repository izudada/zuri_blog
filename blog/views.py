from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

from .models import Post, Comment
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import RegisterForm, AddNewForm, NewCommentForm


class PostTitle(ListView):
    model = Post
    template_name = 'home.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'view_post.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Comment.objects.filter(post=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(body=request.POST.get('body'), author=self.request.user, post=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = ['title', 'body']

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        else:
            return False

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    fields = []
    success_url = reverse_lazy('home')

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        else:
            return False


def profile(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            form = PasswordChangeForm(response.user, response.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(response, user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(response.user)
        return render(response, 'profile.html', {'form' : form})
    else:
        return HttpResponseRedirect("/login/")

def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()

    return render(response, 'register.html', {'form' : form})

def create(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            form = AddNewForm(response.POST)

            if form.is_valid():
                title = form.cleaned_data["title"]
                body = form.cleaned_data["body"]
                post = Post(title=title, body=body)
                post.save()
                response.user.post.add(post)

                return HttpResponseRedirect("/post/%i" %post.id )
            
        else:
            form = AddNewForm
        return render(response, 'new.html', {"form" : form})
    else:
        return HttpResponseRedirect("/login/")