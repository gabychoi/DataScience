from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from loginApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home_post/', views.photo_list, name='photo_list'),
    path('home_post/posting/', views.posting, name='posting'),
    path('comment_create/', views.comment_create, name='comment_create'),
    path('comment_delete/', views.comment_delete, name='comment_delete'),
    path('convert/', views.convert, name='convert'),
    path('profile_img/', views.profile_img, name='profile_img'),
    path('comment_report/', views.comment_report, name='comment_report'),
    path('introduce/', views.introduce, name='introduce'),
    path('user_popup/', views.user_popup, name='user_popup'),
]



from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)