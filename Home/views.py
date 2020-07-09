from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
	return render(request,'Home/home.html')

def profile(request):
	context = { "posts" : Post.objects.all()}
	return render(request,'Home/profile.html', context)

def about(request):
	return render(request,'Home/about.html')

def contact(request):
	return render(request,'Home/contact.html')