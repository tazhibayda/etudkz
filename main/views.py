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
    return render(request , 'main/profile.html',{
        'request':request
    })


def delcomment(request , commentId):
    c = Comment.objects.get(pk=commentId)
    c.delete()
    return redirect("/"+str(c.course_id))

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


def addCom(request,courseid):
    if request.method== 'POST':

        cmnt = request.POST['com']
        c = Course.objects.all().get(pk=courseid)
        name = c.coursename
        teacher = c.teacher
        price = c.price
        comment = Comment.objects.filter(
            Q(course_id=c.pk)
        )
        if not request.user.is_authenticated:
            return render(request, 'main/About.html', {
                'name': name,
                'teacher': teacher,
                'id': price,
                'crsid': courseid,
                'comments': comment,
                'msg': 'You not logged in'
            })
        else:
            com = Comment()
            com.author = request.user.username
            com.course_id = courseid
            com.post = request.POST['post']
            com.text = cmnt
            com.date = timezone.now()
            time = str(com.date.strftime('%H:%M:%S'))
            com.save()
            return render(request, 'main/About.html', {
                'name': name,
                'teacher': teacher,
                'id': price,
                'crsid': courseid,
                'time':com.time,
                'comments': comment,
            })

        return render(request, 'main/About.html', {
            'name': name,
            'teacher': teacher,
            'id': price,
            'crsid': courseid,
            'comments': comment,
        })
    else:
        c = Course.objects.all().get(pk=courseid)
        name = c.coursename
        teacher = c.teacher
        price = c.price
        comment = Comment.objects.filter(
            Q(course_id=c.pk)
        )
        return render(request, 'main/About.html', {
            'name': name,
            'teacher': teacher,
            'id': price,
            'comments': comment,
            'crsid': courseid,
            'msg':'nopost'
        })


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
        if comment.__len__() == 0:

            return render(request,'main/About.html',{
                'name': name,
                'teacher': teacher,
                'id': price,
                'crsid': courseid,
                'comments': comment,
            })
        else:
            return redirect('addcmnt',courseid=courseid)

def chec_learning(request):
    name = request.user.username
    learn_courses = Learning.objects.filter(
        Q(user = name)
    )
    course_name = learn_courses.all()

    return render(request, 'main/Learning.html', {
        'name': name,
        'crs':course_name
    })

def add_to_learning(request, course_id):
    learn = Learning()
    learn.user = request.user.username
    learn.course_id = course_id
    if Learning.objects.filter(course_id=course_id).exists():
        return redirect('addcmnt', courseid=course_id)
    else:
        learn.save()
    return redirect('addcmnt',courseid=course_id)

def delern(request ,courseid):
    learn = Learning.objects.filter(course_id=courseid)
    learn.delete()

    return redirect('learn')

