from django.shortcuts import render,get_object_or_404
from .models import Experience
# Create your views here.


def all_experience(request):
    experiences = Experience.objects.all()
    return render(request, 'experience/all_experience.html', {'experiences': experiences})


def experience_detail(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    return render(request, 'experience/experience_detail.html', {'experience': experience})
