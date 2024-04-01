from django.shortcuts import render
from blog.models import Blog
from .models import Education
from experience.models import Experience
# Create your views here.

def home(request):
    education = Education.objects.order_by('-enddate')
    blog = Blog.objects.order_by('-enddate')
    experience = Experience.objects.all()
    context = {
        'education':education,
        'experience': experience,
        'blog': blog,
    }
    return render(request, 'portfolio/home.html',context)
