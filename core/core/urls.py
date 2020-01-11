"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reloads', views.api_reloads),
    path('filetree', views.api_filetree),
    path('filetree/update', views.api_filetree_update),
    path('file/search', views.api_file_search),
    path('file/summary', views.api_file_summary),
    path('file/refs', views.api_file_refs),
    path('file/fulltxt', views.api_file_fulltxt),
    path('test', views.api_test),
]
