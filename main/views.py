from django.shortcuts import render , HttpResponse

from .models import Course
# Create your views here.

def send(request):
    meets = [
        {'first': 'IP' , 'location' : "kitchen"},
        {'first': 'MP' , 'location' : "Gogolya"},
        {'first': 'Katok' , 'location' : "Medeo"},
    ]

    return render(request , 'main/Card.html' ,{
        'meets' : meets,
    })
def course(request):
    courses = Course.objects.all()
    return render(request , 'main/Card.html',{
        'courses':courses,
    })

def openC(request,courseid):
    if(courseid > Course.objects.all().__len__() or courseid<1):
        return HttpResponse("ERROR")
    else:
        c = Course.objects.all().get(pk=courseid)
        name = c.coursename
        teacher = c.teacher
        price = c.price
        # return HttpResponse(name)
        return render(request,'main/About.html',{
            'name':name,
            'teacher':teacher,
            'id':price,
        })
