import re
from django.shortcuts import render,HttpResponseRedirect , HttpResponse,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
<<<<<<< HEAD
from django.contrib.auth.models import auth,User

from teach.forms import SignUpForm


=======
from main.models import Course
>>>>>>> 169d09daf1e0dae5fc90a39d8f41fb29f39d14c7

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request,user)
            return render(request , 'teach/test_log.html',{
                'username' : username,
            })
        else:
            return render(request , 'teach/login.html',{
                'msg':'Incorrect '
            })
            # return HttpResponse(13)
    else:
        # form = UserCreationForm(request='POST')
        # username = request.POST['username']
        # password = request.POST['password']
        return render(request, 'teach/login.html',{
        })

def logout_view(request):
    logout(request)
    
def index(request):
    return render(request , 'teach/addCourse.html')

def add(request):
    if request.method == 'POST':
        crs = Course()
        coursename = request.POST['coursename']
        teacher = request.POST['teacher']
        price = request.POST['price']
        # courses = Course(coursename,teacher,price)
        # Course.__new__(courses)
        crs.coursename = coursename
        crs.teacher = teacher
        crs.price = price
        crs.save()
        return render(request , 'teach/addCourse.html',{
            'msg':'Added to courses'
        })

def reglog(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']
        return render(request , 'teach/signup.html',{
            'username': username,
            'password': password,
            'confirm':password==confirm,
        })
    

    else:  
        return render(request, 'teach/signup.html')



