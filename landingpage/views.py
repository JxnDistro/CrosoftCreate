from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project
from blog.models import Post
from .forms import SubscriberForm

# Create your views here.
def landingpage(request):
    projects = Project.objects.all()
    posts = Post.objects.filter(status=1)

    posts = posts[:3]
    slide_posts = Post.objects.filter(status=1)[1:]
    latest_post = posts[0]
    context = {
        'projects': projects,
        'posts': posts,
        'slide_posts': slide_posts,
        'latest_post': latest_post
    }
    return render(request, 'home.html', context)

def add_movie(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'movieListChanged'})
    else:
        form = SubscriberForm()
    return render(request, 'movie_form.html', {
        'form': form,
    })
