"""
URL configuration for customerproject project.

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
from customerapp.views import Home,SubmitInput,Submit,Display,DeleteInput,Delete,UpdateInput,UpdateDetails,Update
urlpatterns = [
    path('admin/', admin.site.urls),
    path('customerapp/',Home.as_view()),
    path('customerapp/submitinput',SubmitInput.as_view()),
    path('customerapp/submit',Submit.as_view()),
    path('customerapp/display',Display.as_view()),
    path('customerapp/deleteinput',DeleteInput.as_view()),
    path('customerapp/delete',Delete.as_view()),
    path('customerapp/updateinput',UpdateInput.as_view()),
    path('customerapp/updatedetails',UpdateDetails.as_view()),
    path('customerapp/update',Update.as_view()),

]
