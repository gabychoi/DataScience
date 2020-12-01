from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.hashers import make_password, check_password
from .models import Signup

import re
# Create your views here.


def index(request):
    return render(request, 'loginApp/index.html')


def signup(request):
    if request.method == 'POST' :

        input_name        = request.POST['fullname']
        input_email       = request.POST['email']
        input_password    = request.POST['passsword']
        input_re_password = request.POST['re_passsword']

        print(input_re_password)
        print(input_password)

        if input_password != input_re_password:
            error = '비밀번호가 일치하지 않습니다'
            return render(request, "loginApp/index.html", {'error' : error})

        else :
            database = Signup(user_email = input_email, user_pwd = make_password(input_password), user_name = input_name)
            database.save()
            return HttpResponseRedirect(reverse('index'))


def login(request):
    context= {}
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('index'))

    elif request.method == 'POST':
        input_email = request.POST['email']
        input_password = request.POST['pwd']

        if not (input_email and input_password):
            context['error'] = '아이디와 비밀번호를 모두 입력해주세요'
        else :
            user_db = Signup.objects.get(user_email = input_email)
            if check_password(input_password, user_db.user_pwd) :
                request.session['name'] = user_db.user_name
                return render(request, 'loginApp/home.html')
            else :
                context['error'] = '비밀번호를 틀렸습니다.'
                return render(request, 'loginApp/index.html', context)