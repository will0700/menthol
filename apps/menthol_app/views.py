from django.shortcuts import render, redirect
from apps.login_reg.models import *
from .models import *
# Create your views here.

def dashboard(request): #get
#overview of spending/budget, shows add account/expense anchors/buttons, shows new transfer/payments anchors/buttons
pass

### ACCOUNTS ###
def all_account(request): #get
pass

def add_account(request): #get
pass

def add_account_processing(request): #post - (ex. add a new credit card)
pass
#add view, edit, and remove later :v

### EXPENSES ###
def all_expense(request): #get
pass

def add_expense(request): #get
pass

def add_expense_processing(request): #post - (ex. add a new budget category: Snowboarding)
pass
#add view, edit, and remove later :v

### TRANSFER ###
def all_transfer(request): #get
pass

def new_transfer(request): #get
pass

def new_transfer_processing(request): #post - (new transaction between two accounts, ex. use Checking to pay Credit Card)
pass
#add view, edit, and remove later :v

### PAYMENT ###
def all_payment(request): #get
pass

def new_payment(request): #get
pass

def new_payment_posting(request): #post - (new transaction between expense and account, ex. buy Gas with Credit Card)
pass
#add view, edit, and remove later :v
