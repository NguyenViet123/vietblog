from django.shortcuts import render, get_object_or_404

from.models import About, Post

# Create your views here.

def jinja(request):
	d = {'name': 'Nguyen van viet'}
	return render(request, 'home/home.html', d)

def about(request):
	data = get_object_or_404(About)
	title = data.title
	text = data.text
	time_created = data.created_data

	data_send = {
		"title": title,
		"text" : text,
		"time_created": time_created,
	}

	return render(request, 'home/about.html', data_send)

def posts(request):	
	titles = Post.objects.order_by('-created_data')[:]
	print(titles)
	print(titles[0].title)

	return render(request, 'home/listblog.html', {"titles": titles})

def post(request, id):
	data = get_object_or_404(Post, id=id)
	title = data.title
	text = data.text
	time_created = data.created_data
	author = data.author

	data_send = {
		"author": author,
		"title": title,
		"text" : text,
		"time_created": time_created,
	}


	return render(request, 'home/blog.html', data_send)
