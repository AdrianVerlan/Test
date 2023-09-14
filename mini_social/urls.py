
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from mini_social.views import *


urlpatterns = [
    path("", homePage),
    path("user/home/", homePage),
    path("user/signin/", signinPage),  
    path("user/signup/", signupPage),
    path("user/terms/", termsH),
]

