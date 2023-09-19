from django.urls import re_path as url
from Banking import views

urlpatterns = [
    url(r'^department$', views.departmentApi),
    url(r'^department/([0-9]+)$', views.departmentApi),
    url(r'^department/edit/([0-9]+)$', views.editDepartment),
    url(r'^department/delete/([0-9]+)$', views.deleteDepartment),
    url(r'^employee$', views.employeeApi),
    url(r'^employee/([0-9]+)$', views.employeeApi),
    url(r'^employee/edit/([0-9]+)$', views.editEmployee),
    url(r'^employee/delete/([0-9]+)$', views.deleteEmployee),
    url(r'^customer$', views.customerApi),
    url(r'^customer/([0-9]+)$', views.customerApi),
    url(r'^customer/edit/([0-9]+)$', views.editCustomer),
    url(r'^customer/delete/([0-9]+)$', views.deleteCustomer),
    url(r'^account$', views.accountApi),
    url(r'^account/([0-9]+)$', views.accountApi),
    url(r'^account/edit/([0-9]+)$', views.editAccount),
    url(r'^account/delete/([0-9]+)$', views.deleteAccount),
    url(r'^transaction$', views.transactionApi)
]
