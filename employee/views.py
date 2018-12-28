from django.shortcuts import render, redirect, HttpResponse
import schedule
from employee import models

# Create your views here.
is_admin_login = True
person_bank_id = 0
salary_reflection = {
    13: 14000,
    14: 16000,
    15: 18000,
    16: 230000
}


def check_login_func(request, admin_flag, *html_page):
    global is_admin_login, person_bank_id
    # get input username and password
    login_name = request.POST.get('username', None)
    login_pwd = request.POST.get('password', None)
    if login_name is None:
        error_msg = 'username can not be empty.'
        return render(request, html_page[0][0], {'error_msg': error_msg})
    # get employee_info obj
    if admin_flag:
        manager_info = models.UserInfo.objects.filter(username=login_name, password=login_pwd).first()
    else:
        manager_info = models.EmployeeInfo.objects.filter(username=login_name, password=login_pwd).first()
    if manager_info:
        if admin_flag:
            # admin login #
            is_admin_login = True
        else:
            # personal bank login #
            person_bank_id = manager_info.id
        return redirect(html_page[0][1])
    else:
        error_msg = 'username or password is incorrect.'
        print type(html_page[0][0]), html_page[0][0]
        return render(request, html_page[0][0], {'error_msg': error_msg})


def login(request):
    global is_admin_login
    if 'GET' == request.method:
        return render(request, 'login.html')
    elif 'POST' == request.method:
        result = check_login_func(request, True, ['login.html', '/employee/index/'])
        return result
    else:
        return redirect('/employee/index/')


def logout(request):
    global is_admin_login
    # is_admin_login = False
    error_msg = 'you have logout succeed'
    return render(request, 'login.html', {'error_msg': error_msg})


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
        lev = request.POST.get('level', None)
        if lev is None:
            lev = 0
        else:
            lev = int(lev)
        dep_money = request.POST.get('deposit', None)
        if dep_money is None:
            dep_money = 0
        else:
            dep_money = int(dep_money)
        credit_no = request.POST.get('credit_number', None)
        money_limit = request.POST.get('credit_limit', None)
        available_money = request.POST.get('available_credit', None)
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
            level=lev,
            deposit=dep_money,
            credit_number=credit_no,
            credit_limit=money_limit,
            available_credit=available_money,
        )
        manager_msg = 'update %s succeed' % name
        employee_info = models.EmployeeInfo.objects.all()
        return render(request, 'manager.html', {'employee_info': employee_info, 'manager_msg': manager_msg})
    else:
        return render(request, 'add_employee.html', {'employee_info': employee_info})


def update_employee(request, uid):
    employee_info = models.EmployeeInfo.objects.filter(id=uid).first()
    if 'GET' == request.method:
        return render(request, 'update.html', {'employee_info': employee_info})
    elif 'POST' == request.method:
        new_phone_number = request.POST.get('phone_number', None)
        new_email = request.POST.get('email', None)
        new_address = request.POST.get('address', None)
        new_department = request.POST.get('department', None)
        new_level = request.POST.get('level', None)
        new_deposit = request.POST.get('deposit', None)
        models.EmployeeInfo.objects.filter(id=uid).update(
            phone_number=new_phone_number,
            email=new_email,
            address=new_address,
            department=new_department,
            level=new_level,
            deposit=new_deposit,
        )
        employee = models.EmployeeInfo.objects.filter(id=uid).first()
        manager_msg = 'update %s succeed' % employee.username
        employee_info = models.EmployeeInfo.objects.all()
        return render(request, 'manager.html', {'employee_info': employee_info, 'manager_msg': manager_msg})
    else:
        return render(request, 'update.html', {'employee_info': employee_info})


def delete_employee(request, uid):
    employee_del = models.EmployeeInfo.objects.filter(id=uid).first()
    del_name = employee_del.username
    if 'GET' == request.method:
        return render(request, 'delete.html', {'employee_del': employee_del})
    elif 'POST' == request.method:
        models.EmployeeInfo.objects.filter(id=uid).delete()
        manager_msg = 'delete %s succeed' % del_name
        employee_info = models.EmployeeInfo.objects.all()
        return render(request, 'manager.html', {'employee_info': employee_info, 'manager_msg': manager_msg})
    else:
        return render(request, 'delete.html', {'employee_info': employee_del})


def one_detail_info(request, uid):
    employee_detail = models.EmployeeInfo.objects.filter(id=uid).first()
    return render(request, 'detail.html', {'employee_detail': employee_detail})


def note(request):
    note_contents = models.Notes.objects.all()
    if 'GET' == request.method:
        return render(request, 'note.html', {'note_contents': note_contents})
    if 'POST' == request.method:
        name = request.POST.get('name', None)
        place = request.POST.get('place', None)
        content = request.POST.get('note', None)
        # no. who wheen wheere contents #
        if name == 'lovline':
            name = 'lovline'
        if place == 'home':
            place = 'home'
        models.Notes.objects.create(
            who=name,
            wheere=place,
            contents=content,
        )
    return render(request, 'note.html', {'note_contents': note_contents})


def delete_note(request, del_id):
    models.Notes.objects.filter(id=del_id).delete()
    note_contents = models.Notes.objects.all()
    return render(request, 'note.html', {'note_contents': note_contents})


def person_bank_transaction_func(request, employee, transaction_type):
    employee_info = models.EmployeeInfo.objects.all()
    if employee:
        curr_deposit = employee.deposit
        if 1 == transaction_type:
            # deposit money #
            taken_money = request.POST.get('taken', None)
            if taken_money is None:
                taken_money = 0
            else:
                taken_money = int(taken_money)
                print taken_money
            if taken_money >= curr_deposit:
                error_msg = 'sorry you dont have enough money to take'
            else:
                up_deposit = curr_deposit - taken_money
                print up_deposit
                models.EmployeeInfo.objects.filter(id=person_bank_id).update(deposit=up_deposit)
                error_msg = 'you have taken %d money from your bank account' % taken_money
            return render(request, 'personal_bank_service.html', {'error_msg': error_msg, 'employee_info': employee_info})
        elif 2 == transaction_type:
            # draw money #
            save_money = request.POST.get('save', None)
            if save_money is None:
                save_money = 0
            else:
                save_money = int(save_money)
            up_deposit = curr_deposit + save_money
            models.EmployeeInfo.objects.filter(id=person_bank_id).update(deposit=up_deposit)
            error_msg = 'you have save %d money to your bank account' % save_money
            return render(request, 'personal_bank_service.html', {'error_msg': error_msg, 'employee_info': employee_info})
        elif 3 == transaction_type:
            # transfer money #
            transfer_money = request.POST.get('transfer', None)
            if transfer_money is None:
                transfer_money = 0
            else:
                transfer_money = int(transfer_money)
            to_person_id = int(request.POST.get('to_person', None))
            to_person_obj = models.EmployeeInfo.objects.filter(id=to_person_id).first()
            if transfer_money >= curr_deposit:
                error_msg = 'sorry you dont have enough money to take'
            else:
                up_deposit = curr_deposit - transfer_money
                models.EmployeeInfo.objects.filter(id=person_bank_id).update(deposit=up_deposit)
                to_person_deposit = to_person_obj.deposit + transfer_money
                models.EmployeeInfo.objects.filter(id=to_person_id).update(deposit=to_person_deposit)
                error_msg = 'you have transfered %d money to %s from your bank account' % (
                    transfer_money, to_person_obj.username)
            return render(request, 'personal_bank_service.html', {'error_msg': error_msg, 'employee_info': employee_info})
        else:
            pass
    else:
        return render(request, 'personal_bank_service.html')


def personal_bank_service(request):
    global person_bank_id
    employee_info = models.EmployeeInfo.objects.all()
    employee = models.EmployeeInfo.objects.filter(id=person_bank_id).first()
    if employee is None:
        error_msg = 'please login first to your Bank'
        return render(request, 'bank_service_login.html', {'error_msg': error_msg})
    if 'GET' == request.method:
        return render(request, 'personal_bank_service.html', {'employee': employee, 'employee_info': employee_info})
    elif 'POST' == request.method:
        transaction_type = request.POST.get('transaction_type', None)
        result = person_bank_transaction_func(request, employee, int(transaction_type))
        return result
    else:
        return redirect('/employee/personal_bank_service/')


def bank_service_login(request):
    if 'GET' == request.method:
        return render(request, 'bank_service_login.html')
    elif 'POST' == request.method:
        result = check_login_func(request, False, ['bank_service_login.html', '/employee/personal_bank_service/'])
        return result
    else:
        return redirect('/employee/bank_service_login/')


def credit_card(request):
    employee_info = models.EmployeeInfo.objects.all()
    if 'GET' == request.method:
        return render(request, 'credit_card.html', {'employee_info': employee_info})
    elif 'POST' == request.method:
        increase_person_id = request.POST.get('increase_person', None)
        increase_limit = request.POST.get('increase_limit', None)
        employee = models.EmployeeInfo.objects.filter(id=int(increase_person_id)).first()
        if employee:
            up_limit = employee.credit_limit + int(increase_limit)
            models.EmployeeInfo.objects.filter(id=int(increase_person_id)).update(credit_limit=up_limit)
            employee = models.EmployeeInfo.objects.filter(id=int(increase_person_id)).first()
            error_msg = 'increase Credit Limit of %s is succeed ,current limt is %s' % (employee.username, employee.credit_limit)
            return render(request, 'credit_card.html', {'error_msg': error_msg, 'employee_info': employee_info})
        else:
            return render(request, 'credit_card.html')
    else:
        return redirect('/employee/credit_card/')


def shop_store(request):
    if 'GET' == request.method:
        return render(request, 'shop_store.html')
    elif 'POST' == request.method:
        book_list = []
        for book in request.POST.getlist('books'):
            book_list.append(book)
        error_msg = 'shop store is developing.'
        # TODO #
        return render(request, 'credit_card.html', {'error_msg': error_msg, 'book_list': book_list})
    else:
        return redirect('/employee/index/')


def record_history(request):
    pass


def add_manager(request):
    result = models.UserInfo.objects.all()
    for row in result:
        print row.username, row.password
    return HttpResponse('<h1>add manager ok.</h1>')


def payment_remuneration_timed_task():
    global is_admin_login, salary_reflection
    if is_admin_login:
        employee_objs = models.EmployeeInfo.objects.all()
        for employee in employee_objs:
            curr_emp_id = employee.id
            curr_emp_salary = employee.deposit
            salary_increase = salary_reflection[employee.level]
            if salary_increase is None:
                salary_increase = 0
            money = curr_emp_salary + salary_increase
            models.EmployeeInfo.objects.filter(id=curr_emp_id).update(deposit=money)


if __name__ == '__main__':
    # payment_remuneration_timed_task of 10 minutes#
    schedule.every(10).minutes.do(payment_remuneration_timed_task)
    while True:
        schedule.run_pending()

