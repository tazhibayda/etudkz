from urllib import request
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
import re
from django.shortcuts import render,HttpResponseRedirect , HttpResponse,redirect
from main.models import Course
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# from django. import response
from django.template import response
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import auth,User
from teach.forms import SignUpForm
from main.models import Course
from django.views import generic





def account(request):

    if request.user.is_authenticated:
        return render(request, 'teach/account.html',{
            'username':request.user.username
        })
    else:
        return render(request, 'teach/login.html')


def liked(request):
    courses = Course.objects.all().filter(

    )
    return render(request , 'teach/liked1.html',{
        'courses':courses,
        'request':request,
    })

def login_view(request):
    boo = request.user.is_authenticated
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request,user)
            return render(request, 'main/header.html', {
                'request': request
            })

        else:
            return render(request , 'teach/login.html',{
                'msg':'Incorrect '
            })
            # return HttpResponse(13)
    else:
        return render(request, 'teach/login.html',{
        })

def logout_view(request):
    logout(request)
    
def index(request):
    boo = request.user.is_authenticated
    if boo and request.user.is_superuser:
        return render(request , 'teach/addCourse.html')
    else :
        return render(request,'main/header.html')

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
    if request.user.is_superuser:
        return render(request,'teach/addCourse.html')
    else :
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            user = request.POST['username']
            if User.objects.filter(username=user).exists():
                # print(12312321)
                return render(request, 'teach/signup.html',{
                    'msg':'User already exists plaese choose another username',
                    'form':form,
                })
            elif form.is_valid():
                form.save()
            else:
                return render(request, 'teach/signup.html', {
                    'msg': 'Your password or username entered incorrectly',
                    'form': form,
                })
        form = UserCreationForm()
        return render(request, 'teach/signup.html' , {
            'form':form
        })

def regist(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            form = UserCreationForm()

    return render(request, 'teach/regorlog.html' , {
        'form':form
    })


class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'teach/edit_profile.html'
    success_url = reverse_lazy('account')

    def get_object(self):
        return self.request.user


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
# =======
#
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         confirm = request.POST['confirm']
#         return render(request , 'teach/signup.html',{
#             'username': username,
#             'password': password,
#             'confirm':password==confirm,
#         })
#
#
#     else:
#         return render(request, 'teach/signup.html')
#

# >>>>>>> 8405947f5850499c4ec15157c8510f21c27a7a30

