from.import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.loginn,name='login'),
    path('form',views.form,name='form'),
    path('forum',views.forum,name='forum'),
    path('fill',views.fill,name='fill')

]
