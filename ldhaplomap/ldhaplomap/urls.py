"""
URL configuration for ldhaplomap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#from django.conf.urls import url
from django.conf.urls import include
from django.conf import settings
from rest_framework import permissions
from serolizer import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Web services interface information for Transplanttoolbox",
        default_version='v1',
        contact=openapi.Contact(email="lgragert@tulane.edu"),
    ),
    #url="https://www.transplanttoolbox.org/cpra_home/services",
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('',views.ld_haplo_input,name='ld_haplo_home'),
    path('serolizer_out/',views.ld_haplo_out,name='ld_haplo_out'),
]
