from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from loginApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.login, name='login'),
    path('home_post/', views.photo_list, name='photo_list'),
    path('home_post/posting', views.posting, name='posting'),
    path('home_comment_posting', views.comment_posting, name='comment_posting')
]



from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)