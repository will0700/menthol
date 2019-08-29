from django.db import models
from apps.login_reg.models import *

class Account(models.Model):
    name = models.CharField(max_length=45) #ex. BoA Checking, Chase CC, etc
    acc_balance = models.DecimalField(decimal_places=2)
    category = models.CharField(max_length=45) #only checking, saving, credit_card |for now|Venmo as reach goal|
    owner = models.ForeignKey(User, related_name="accounts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Expense(models.Model):
    name = models.CharField(max_length=45) #ex. Food, Gas, Shopping, etc
    exp_balance = models.DecimalField(decimal_places=2)
    budget = models.DecimalField(decimal_places=2)
    owner = models.ForeignKey(User, related_name="expenses")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Payment(models.Model):
    vendor = models.CharField(max_length=45) #ex. Taco Bell, Nordstrom, etc
    description = models.CharField(max_length=45) #ex. New red flannel, lunch with Eduardo, etc
    payment_amount = models.DecimalField(decimal_places=2)
    debit_exp = models.ForeignKey(Expense, related_name="payments_debit")
    credit_acc = models.ForeignKey(Account, related=name="payments_credit")
    owner = models.ForeignKey(User, related_name="expenses")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Transfer(models.Model):
    vendor = models.CharField(max_length=45) #ex. Taco Bell, Nordstrom, Chase Bank, etc
    description = models.CharField(max_length=45) #ex. Pay Chase Card off with BoA Checking, Buy Gas at Arco with Debit Card, etc
    transfer_amount = models.DecimalField(decimal_places=2)
    debit_acc = models.ForeignKey(Account, related_name="transfers_debit")
    credit_acc = models.ForeignKey(Account, related_name="transfers_credit")
    owner = models.ForeignKey(User, related_name="expenses")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

