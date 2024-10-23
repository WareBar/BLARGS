from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #to prevent accessing a page without being authenticated or logged in

#import model object
from .models import Post

#import forms
from . import forms


def post_list(request):
	# collects all objects inside of the Post Class
	# since Post Class are like a list/array of an objects
	Posts = Post.objects.all()
	return render(request, "POSTS/post_list.html",{
		'Posts':Posts
		})


def post_page(request, slug):
	# collects one instance only based on the field provided
	# if two instance matched or find, it will throw an error becuase .get() should only fetch one instance
	specificPost = Post.objects.get(slug=slug)
	return render(request, "POSTS/post_page.html",{
		"specificPost":specificPost
		})




# this decorator requires the user to be authenticated, if not, they will be redirected to the given path
@login_required(login_url='/users/login/')
def post_new(request):
	if request.method == "POST":
		form = forms.createPost(request.POST, request.FILES)
		if form.is_valid():
			# manually filling the author field since that field is not included in the forms and therefore the request does not contain the author value
			# 'commit=False' this allow us to save the form but postpone or stop the value of the form to be saved in the database
			form_author = form.save(commit=False)
			form_author.author = request.user
			form_author.save()
			form.save()
			return redirect('POST:list')
	else:
		form = forms.createPost()

	return render(request, 'POSTS/post_new.html',{
		"form":form
		})


