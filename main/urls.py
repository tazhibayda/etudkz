from django.urls import path

from . import views

urlpatterns = [
    path('' , views.course),
    path('<int:courseid>' , views.openC),
]