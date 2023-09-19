from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

from Banking.models import Departments, Employees, Customers, Accounts, Transactions
from Banking.serializers import DepartmentSerializer, EmployeeSerializer, CustomerSerializer, AccountSerializer, TransactionSerializer

# Create your views here.


@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        departments_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    # elif request.method == 'PUT':
    #     department_data = JSONParser().parse(request)
    #     department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
    #     departments_serializer = DepartmentSerializer(department,data=department_data)
    #     if departments_serializer.is_valid():
    #         departments_serializer.save()
    #         return JsonResponse("Update Successfully",safe=False)
    #     return JsonResponse("Failed to Update",safe=False)
    # elif request.method == 'DELETE':
    #     department = Departments.objects.get(DepartmentId=id)
    #     department.delete()
    #     return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
def editDepartment(request, id=0):
    if request.method == 'POST':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(
            DepartmentId=department_data['DepartmentId'])
        departments_serializer = DepartmentSerializer(
            department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
    return JsonResponse("Failed to Update", safe=False)


@csrf_exempt
def deleteDepartment(request, id=0):
    if request.method == 'POST':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)


@csrf_exempt
def editEmployee(request, id=0):
    if request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees = Employees.objects.get(
            EmployeeId=employee_data['EmployeeId'])
        employees_serializer = EmployeeSerializer(
            employees, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
        return JsonResponse("Update Successfully", safe=False)
    return JsonResponse("Failed to Update", safe=False)


@csrf_exempt
def deleteEmployee(request, id=0):
    if request.method == 'POST':
        employees = Employees.objects.get(EmployeeId=id)
        employees.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def customerApi(request, id=0):
    if request.method == 'GET':
        customers = Customers.objects.all()
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customers_serializer = CustomerSerializer(data=customer_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)


@csrf_exempt
def editCustomer(request, id=0):
    if request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customers = Customers.objects.get(
            CustomerId=customer_data['CustomerId'])
        customers_serializer = CustomerSerializer(
            customers, data=customer_data)
        if customers_serializer.is_valid():
            customers_serializer.save()
        return JsonResponse("Update Successfully", safe=False)
    return JsonResponse("Failed to Update", safe=False)


@csrf_exempt
def deleteCustomer(request, id=0):
    if request.method == 'POST':
        customers = Customers.objects.get(CustomerId=id)
        customers.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def accountApi(request, id=0):
    if request.method == 'GET':
        accounts = Accounts.objects.all()
        accounts_serializer = AccountSerializer(accounts, many=True)
        return JsonResponse(accounts_serializer.data, safe=False)
    elif request.method == 'POST':
        account_data = JSONParser().parse(request)
        accounts_serializer = AccountSerializer(data=account_data)
        if accounts_serializer.is_valid():
            accounts_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)


@csrf_exempt
def editAccount(request, id=0):
    if request.method == 'POST':
        account_data = JSONParser().parse(request)
        accounts = Accounts.objects.get(
            AccountId=account_data['AccountId'])
        accounts_serializer = AccountSerializer(
            accounts, data=account_data)
        if accounts_serializer.is_valid():
            accounts_serializer.save()
        return JsonResponse("Update Successfully", safe=False)
    return JsonResponse("Failed to Update", safe=False)


@csrf_exempt
def deleteAccount(request, id=0):
    if request.method == 'POST':
        accounts = Accounts.objects.get(AccountId=id)
        accounts.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def transactionApi(request, id=0):
    if request.method == 'GET':
        transactions = Transactions.objects.all()
        transactions_serializer = TransactionSerializer(
            transactions, many=True)
        return JsonResponse(transactions_serializer.data, safe=False)
