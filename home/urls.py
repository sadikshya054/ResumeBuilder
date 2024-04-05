from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name= 'welcome'),
    path('login/', views.user_login, name= 'login'),
    path('register/', views.register, name= 'register'),
    path('home/', views.home, name= 'home'),
    path('form-submit/', views.submit_form, name= 'submit_form'),
    path('file-sent/', views.file_sent, name='file_sent'),
    path('logout/', views.logout_view, name= 'logout')
]