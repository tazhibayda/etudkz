from django.urls import path

from . import views

urlpatterns = [
    path('' , views.course),
    path('<int:courseid>' , views.openC),
    path('del/<int:courseid>' , views.delete  , name='delete'),
    path('result' , views.srch, name='searching')
]