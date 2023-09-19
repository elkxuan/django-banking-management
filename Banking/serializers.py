from rest_framework import serializers
from Banking.models import Departments, Employees, Customers, Accounts, Transactions


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId', 'DepartmentName')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId', 'EmployeeName', 'EmployeePhone',
                  'EmployeeEmail', 'Department')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ('CustomerId', 'CustomerName', 'CustomerPhone',
                  'CustomerEmail', 'CustomerAddress', 'AccountNumber')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('AccountId','AccountNumber', 'AccountType',
                  'CustomerId', 'Balance', 'Status')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('TransactionId', 'AccountNumber',
                  'TransactionDate', 'TransactionType', 'Status')
