from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "all_courses" : Course.objects.all()
    }
    print Course.objects.all()
    for course in Course.objects.all():
        print "each course object", course.name, course.description
    return render(request, 'classroom/index.html', context)

def add(request):
    valid, response = Course.objects.addClass(request.POST)
    if not valid:
        
        messages.error(request, response)


    return redirect('/')

def delete(request, id):
    context = {
        "deletedcourse" : Course.objects.filter(id = id),
    }
    return render(request, 'classroom/deletepage.html', context)

def finaldelete(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
