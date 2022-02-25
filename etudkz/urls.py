from django.contrib import admin
from django.urls import path, include

import main

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('teach/', include('teach.urls')),

]


