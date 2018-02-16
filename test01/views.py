# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib import auth

from .models import Post
from .forms import PostForm
from django.core.urlresolvers import reverse

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.

User = get_user_model()


def all_users(request):
	user = auth.get_user(request)
	if user.is_authenticated:
		users_all = User.objects.all()
		return render(request, 'index_main.html', {"users_all": users_all})
	else:
		return redirect("/admin/")
		


def user_posts(request, pk):
	user = auth.get_user(request)
	if user.is_authenticated:
		posts = Post.objects.filter(author=pk)
		return render(request, 'personal_post.html', {"posts": posts})
	else:
		return redirect("/admin/")

def post_id(request, id):
	user = auth.get_user(request)
	if user.is_authenticated:
		post = get_object_or_404(Post, id=id)
		return render(request, 'post_id.html', {"post": post})
	else:
		return redirect("/admin/")
	

# class PostView(TemplateView):
#     template_name = 'post_id.html'

#     def get_context_data(self, **kwargs):
# 		post = Post.objects.get(id=kwargs.get('id'))
#     	return { "post": post }


class CreatePostView(CreateView):
	#model = Post
	#fields = ['title', 'description', 'public', 'author']
	#success_url = '/blog/users/'
	form_class = PostForm
	template_name = 'post/create_post.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(CreatePostView, self).form_valid(form) #response


	def get_success_url(self):
		return reverse("main")
   
class UpdatePostView(UpdateView):
	model = Post
	#fields = ['title', 'description', 'public', 'author']
	form_class = PostForm
	template_name = 'post/create_post.html'

	def form_valid(self, form):
		response = super(UpdatePostView, self).form_valid(form)
		self.object = form.save()
		return super(UpdatePostView, self).form_valid(form)      

	def get_success_url(self):
		return reverse("main")        