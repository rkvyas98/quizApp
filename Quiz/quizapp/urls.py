from django.contrib import admin
from django.urls import path
from quizapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/<str:sub>', views.quiz, name='quiz'),
    path('tests_stats', views.tests_stats, name='tests_stats'),
    path('signup/', views.handleSignup, name='handleSignup'),    
    path('login/', views.handleLogin, name='handleLogin'),    
    path('logout/', views.handleLogout, name='handleLogout'),    
    path('student', views.student, name='student'),    
    path('teacher', views.teacher, name='teacher')
    # path('insert_data', views.insert_data, name='insert_data'),
]
