
from django.urls import path
from loginApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.login, name='login')
]