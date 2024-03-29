"""one2one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from app07 import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="index.html"),name="main"),
    path('addPE/',views.addPE,name="addPE"),
    path('savepe/',views.savePE,name="savepe"),
    path('viewPE/',views.viewPE,name="viewPE"),
    path('addPAS/',views.addPAS,name="addPAS"),
    path('savePAS/', views.savePAS, name="savePAS"),
    path('viewPAS/', views.viewPAS, name="viewPAS"),

]
