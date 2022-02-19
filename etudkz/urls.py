from django.contrib import admin
from django.urls import path, include

import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('main.urls')),
]


