from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm
# from django. import response
from django.template import response
from django.urls import reverse
from main.models import Course
from .models import Teacher
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request,user)
            return HttpResponse("Hello "+username)
            # return render(request , 'teach/login.html')
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
        #     'username': username,
        #     'password': password,
        #
        })


def index(request):
    return render(request , 'teach/addCourse.html')

def add(request):
    if request.method == 'POST':
        crs = Course()
        coursename = request.POST['coursename']#Ibek
        teacher = request.POST['teacher']#FizX
        price = request.POST['price']#400

        crs.coursename = coursename
        crs.teacher = teacher
        crs.price = price
        crs.save()
        return render(request , 'teach/addCourse.html',{
            'msg':f"Added to courses {coursename}, {teacher}, {price}"
        })

def reglog(request):
    form = UserCreationForm()
    return render(request, 'teach/signup.html' ,{
        'form':form
    } )
    # if request.method == 'POST':
        # form = UserCreationForm(request='POST')
        # if form.is_valid():
        #     form.save()
        # username = request.POST['username']
        # email = request.POST['email']
        # password = request.POST['password']
        # confirm = request.POST['confirm']

        # form = Teacher(request.POST)

        # if form.is_valid():
        #     form.save()
        #
        #
        #     return redirect('login')
        #     return render(request, 'teach/signup.html',{
        #         'msg':'Successful'
            # })
        # else:
        #     form = Teacher()
            # return render(request , 'teach/signup.html',{
            #     'username': username,
            #     'email': email,
            #     'password': password,
            #     'confirm':password==confirm,
            #
            # })
    # else:
    #     return render(request, 'teach/signup.html',{'form':form})
    # else:
    #     return render(request, 'teach/signup.html')

