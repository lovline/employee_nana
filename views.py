from django.shortcuts import render, redirect, HttpResponse
from employee import models
# Create your views here.
is_admin_login = False


def login(request):
    global is_admin_login
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
            is_admin_login = True
            return redirect('/employee/index/')
        else:
            error_msg = 'username or password is incorrect.'
            return render(request, 'login.html', {'error_msg': error_msg})
    else:
        return redirect('/employee/index/')


def index(request):
    global is_admin_login
    if is_admin_login is False:
        error_msg = 'please login first'
        return render(request, 'login.html', {'error_msg': error_msg})
    return render(request, 'index.html')


def manager_employee(request):
    employee_info = models.EmployeeInfo.objects.all()
    return render(request, 'manager.html', {'employee_info': employee_info})


def add_employee(request):
    employee_info = models.EmployeeInfo.objects.all()
    if 'GET' == request.method:
        return render(request, 'add_employee.html', {'employee_info': employee_info})
    elif 'POST' == request.method:
        name = request.POST.get('username', None)
        pwd = request.POST.get('password', None)
        age = request.POST.get('age', None)
        gender_value = request.POST.get('gender', None)
        gender = 'Male'
        if 2 == int(gender_value):
            gender = 'Female'
        elif 3 == int(gender_value):
            gender = 'two-in-one'
        phone_number = request.POST.get('phone_number', None)
        email = request.POST.get('email', None)
        interests_value = request.POST.getlist('interests', None)
        interests_list = []
        for value in interests_value:
            inter = 'coding'
            if 1 == int(value):
                inter = 'coding'
            elif 2 == int(value):
                inter = 'reading'
            elif 3 == int(value):
                inter = 'sleeping'
            interests_list.append(inter)
        interests_str = str(interests_list)
        address = request.POST.get('address', None)
        school = request.POST.get('school', None)
        department = request.POST.get('department', None)
        models.EmployeeInfo.objects.create(
            username=name,
            password=pwd,
            age=age,
            gender=gender,
            phone_number=phone_number,
            email=email,
            interests=interests_str,
            address=address,
            school=school,
            department=department,
        )
        manager_msg = 'update %s succeed' % name
        employee_info = models.EmployeeInfo.objects.all()
        return render(request, 'manager.html', {'employee_info': employee_info, 'manager_msg': manager_msg})
    else:
        return render(request, 'add_employee.html', {'employee_info': employee_info})


def employee_login(request):
    pass


def employee_logout(request):
    pass


def update_employee(request, uid):
    employee_info = models.EmployeeInfo.objects.filter(id=uid).first()
    if 'GET' == request.method:
        return render(request, 'update.html', {'employee_info': employee_info})
    elif 'POST' == request.method:
        new_phone_number = request.POST.get('phone_number', None)
        new_email = request.POST.get('email', None)
        new_address = request.POST.get('address', None)
        new_department = request.POST.get('department', None)
        models.EmployeeInfo.objects.filter(id=uid).update(
            phone_number=new_phone_number,
            email=new_email,
            address=new_address,
            department=new_department,
        )
        employee = models.EmployeeInfo.objects.filter(id=uid).first()
        manager_msg = 'update %s succeed' % employee.username
        employee_info = models.EmployeeInfo.objects.all()
        return render(request, 'manager.html', {'employee_info': employee_info, 'manager_msg': manager_msg})
    else:
        return render(request, 'update.html', {'employee_info': employee_info})


def delete_employee(request):
    pass


def one_detail_info(request, uid):
    employee_detail = models.EmployeeInfo.objects.filter(id=uid).first()
    return render(request, 'detail.html', {'employee_detail': employee_detail})


def note(request):
    pass


def bank_service(request):
    pass


def shop_store(request):
    pass


def record_history(request):
    pass


def add_manager(request):
    result = models.UserInfo.objects.all()
    for row in result:
        print row.username, row.password
    return HttpResponse('<h1>add manager ok.</h1>')


