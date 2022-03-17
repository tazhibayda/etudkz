from django.urls import path

from . import views

urlpatterns = [
    path('' , views.course , name = 'course'),
    path('<int:courseid>' , views.openC),
    path('del/<int:courseid>' , views.delete  , name='delete'),
    path('result' , views.srch, name='searching'),
    path('logout', views.logout_view , name = 'logout' ),
    path('<int:courseid>/addcmnt', views.addCom , name='addcmnt'),
    path('delcom/<int:commentId>',views.delcomment ,name='delcom')
]