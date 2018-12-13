from django.shortcuts import render, redirect, HttpResponse
from employee import models
# Create your views here.


def login(request):
    if 'GET' == request.method:
        return render(request, 'login.html')
    elif 'POST' == request.method:
        # get input username and password
        login_name = request.POST.get('username', None)
        login_pwd = request.POST.get('password', None)
        if login_name is None:
            error_msg = 'username can not be empty.'
            return render(request, 'login.html', {'error_msg': error_msg})
        # get admin_info obj
        manager_info = models.UserInfo.objects.filter(username=login_name, password=login_pwd).first()
        if manager_info:
            return redirect('/employee/index/')
        else:
            error_msg = 'username or password is incorrect.'
            return render(request, 'login.html', {'error_msg': error_msg})
    else:
        return redirect('/employee/index/')


def add_manager(request):
    result = models.UserInfo.objects.all()
    for row in result:
        print row.username, row.password
    return HttpResponse('<h1>add manager ok.</h1>')


def index(request):
    return render(request, 'index.html')