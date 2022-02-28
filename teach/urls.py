from django.urls import path,include

from . import views

urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('',views.index, name='index'),
    path('test/',views.reglog , name='reglog'),
]