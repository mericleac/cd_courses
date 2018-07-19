from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'index.html', { 'courses': Course.objects.all() })

def new(request):
    course = Course(name=request.POST['name'], description=request.POST['description'])
    course.save()

    return redirect('/courses')

def confirm_delete(request, id):
    course = Course.objects.get(id=id)

    return render(request, 'confirm.html', { 'course': course })

def destroy(request, id):
    course = Course.objects.get(id=id)
    course.delete()

    return redirect('/courses')
