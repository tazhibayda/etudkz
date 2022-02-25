from django.shortcuts import render,HttpResponseRedirect , HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.urls import reverse


# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request,user)

            # return render(request , 'teach/login.html')
        else:
            return HttpResponse(123)
            # return HttpResponse(13)
    else:
        return render(request, 'teach/login.html')


def index(request):
    return HttpResponse('Hello, World')

