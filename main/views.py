from django.shortcuts import render , HttpResponse,redirect

from .models import Course
# Create your views here.
from django.db.models import Q

def course(request):
    courses = Course.objects.all()
    return render(request , 'main/Card.html',{
        'courses':courses,
    })

def delete(request , courseid):
    crs = Course.objects.get(id=courseid)
    crs.delete()
    courses = Course.objects.all()
    return render(request, 'main/Card.html',{
        'courses':courses,
    })

def srch(request ):
    courses = Course.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        m = Course.objects.filter(
            Q(coursename__contains=name)
        )
        return render(request, 'main/Card.html',{
            'courses':m
        })
    else:
        return render(request, 'main/Card.html',{
            'courses':courses
        });

def openC(request,courseid):
    len = Course.objects.all().last().id

    # if not Course.objects.contains():

    if(courseid > len or courseid<1):
        return HttpResponse("ERROR")
    else:
        c = Course.objects.all().get(pk=courseid)
        name = c.coursename
        teacher = c.teacher
        price = c.price
        return render(request,'main/About.html',{
            'name':name,
            'teacher':teacher,
            'id':price,
        })
# <<<<<<< HEAD//
# =======
#

# >>>>>>> 169d09daf1e0dae5fc90a39d8f41fb29f39d14c7
