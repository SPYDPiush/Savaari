from django.contrib import admin
from django.urls import path,include
from .views import sign_up
# from authorization imp
urlpatterns = [
    path('sign-up',sign_up),
]