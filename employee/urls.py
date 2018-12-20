"""employee_nana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from employee import views

urlpatterns = [
    url(r'^add_manager/', views.add_manager),
    url(r'^add_employee/', views.add_employee),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^index', views.index),
    url(r'^manager_employee', views.manager_employee),
    url(r'^update_(\d+)/', views.update_employee),
    url(r'^delete_(\d+)/', views.delete_employee),
    url(r'^detail_(\d+)', views.one_detail_info),
    url(r'^note', views.note),
    url(r'^bank_service_login', views.bank_service_login),
    url(r'^personal_bank_service', views.personal_bank_service),
    url(r'^shop_store', views.shop_store),
    url(r'^record_history', views.record_history),
]
