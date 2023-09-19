from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=255)
    EmployeePhone = models.CharField(max_length=20)
    EmployeeEmail = models.CharField(max_length=255)
    Department = models.CharField(max_length=255)

class Customers(models.Model):
    CustomerId = models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=255)
    CustomerPhone = models.CharField(max_length=20)
    CustomerEmail = models.CharField(max_length=255)
    CustomerAddress = models.CharField(max_length=255)
    AccountNumber = models.IntegerField()

class Accounts(models.Model):
    AccountId = models.AutoField(primary_key=True)
    AccountNumber = models.IntegerField()
    AccountType = models.CharField(max_length=255)
    CustomerId = models.CharField(max_length=255)
    Balance = models.DecimalField(max_digits=10, decimal_places=2)
    Status = models.CharField(max_length=255)

class Transactions(models.Model):
    TransactionId = models.AutoField(primary_key=True)
    AccountNumber = models.IntegerField()
    TransactionDate = models.DateField()
    TransactionType = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)
