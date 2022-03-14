from django.contrib.auth import logout
from django.shortcuts import render , HttpResponse,redirect

from .models import *
# Create your views here.
from django.db.models import Q

def course(request):
    courses = Course.objects.all()

    return render(request , 'main/Card.html',{
        'courses':courses,
    })

def header(request):
    boo = request.user.is_authenticated()
    return render(request , 'main/header.html',{
        'request':request
    })


def logout_view(request):
    logout(request)
    return render(request,'teach/login.html')

def delete(request , courseid):
    crs = Course.objects.get(id=courseid)
    crs.delete()
    return redirect('course')




def srch(request ):
    courses = Course.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        m = Course.objects.filter(
            coursename__contains=name
        )
        list = []
        for el in m:
            list.append(el)

        l = Course.objects.filter(
            teacher__contains=name
        )

        for el in l:
            if not list.__contains__(el):
                list.append(el)
        return render(request, 'main/Card.html',{
            'courses':list
        })
    else:
        return render(request, 'main/Card.html',{
            'courses':courses
        });


def addCom(request):
    if request.method== 'POST':

        cmnt = request.POST['com']
        return

def openC(request,courseid):
    len = Course.objects.all().last().id


    if(courseid > len or courseid<1):
        return HttpResponse("ERROR")
    else:
        c = Course.objects.all().get(pk=courseid)
        name = c.coursename
        teacher = c.teacher
        price = c.price
        comment = Comment.objects.filter(
            Q(course_id=c.pk)
        )
        return render(request,'main/About.html',{
            'name':name,
            'teacher':teacher,
            'id':price,
            'comments':comment
        })
