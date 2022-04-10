from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('',views.index, name='index'),
    path('test/',views.reglog , name='reglog'),
    path('add', views.add , name = 'add'),
    path('account', views.account, name = 'account'),
    path('liked', views.liked, name = 'liked1'),
    path('edit_profile/',views.UserEditView.as_view(),name='edit_profile')
]
urlpatterns += staticfiles_urlpatterns()