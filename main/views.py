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
    #     [
    #     {'coursename': 'Back-End','teacher':'mr Bissenbay' , 'price':1099},
    #     {'coursename': 'Front-End','teacher':'Duman Telman' , 'price':699},
    #     {'coursename': 'Full-Stack','teacher':'mr Unknown' , 'price':1499},
    #     {'coursename': 'Algos','teacher':'Yerbol Baygaraev' , 'price':2599},
    #     {'coursename': 'Play','teacher':'Somehow' , 'price':799},
    #     {'coursename': 'Dota 2','teacher':'Miracle-' , 'price':0},
    #     {'coursename': 'Dota 2','teacher':'Miracle-' , 'price':399},
    #     {'coursename': 'Dota 2','teacher':'Miracle-' , 'price':399},
    #     {'coursename': 'CS GO','teacher':'S1mple-' , 'price':99},
    #     {'coursename': 'CS GO','teacher':'S1mple-' , 'price':99},
    #     {'coursename': 'CS GO','teacher':'S1mple-' , 'price':99},
    #     {'coursename': 'CS GO','teacher':'S1mple-' , 'price':99},
    #     {'coursename': 'CS GO','teacher':'S1mple-' , 'price':99},
    #     {'coursename': 'CS GO','teacher':'S1mple-' , 'price':99},
    # ]
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
        return render(request,'main/About.html')