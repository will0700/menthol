from django.shortcuts import render, redirect
from apps.login_reg.models import *
from .models import *



#################
### DASHBOARD ###
#################
def dashboard(request): #please proofread and replace this comment with "#complete" -Will
    if "user_id" not in request.session:
        return redirect('/')
    else:
        context {
            "user": User.objects.get(id=request.session["user_id"]),
            "all_accounts": Account.objects.all(),
            "all_expenses": Expense.objects.all(),
            "all_payments": Payment.objects.all(),
            "all_transfers": Transfer.objects.all(),
        }
        return render(request, 'menthol_app/dashboard.html', context)



################
### ACCOUNTS ###
################
def all_account(request): #please proofread and replace this comment with "#complete" -Will
    if "user_id" not in request.session:
        return redirect('/')
    else:
        owner = User.objects.get(id=request.session["user_id"])
        all_accounts = Account.object.filter(owner=owner)
        context = {
            "user": owner,
            "all_accounts": all_accounts,
        }
        return render(request, 'menthol_app/al_account.html', context)

def add_account(request): #please proofread and replace this comment with "#complete" -Will
    if "user_id" not in request.session:
        return redirect('/')
    else:
        context = {
            "user": User.objects.get(id=request.session["user_id"]), #idk if needed, but safe -Will
        }
        return render(request, '/menthol_app/dashboard.html', context)

def add_account_processing(request): #please proofread and replace this comment with "#complete" -Will
    if request.method != "POST":
        return redirect('/accounts/new')
    form = request.POST
    owner = User.objects.get(id = request.session['user_id'])
    new_account = Account.objects.create(name = form['name'], acc_balance = form['initial_balance'], category = form['category'], owner = owner)
    return redirect("/dashboard") # /dashboard or /accounts? You guys's UX decision. -Will

#To Do: View, Edit, Remove
###
### I know we didn't want multiple templates redirecting everywhere for UX reasons, but I think we at least need one template between View and Edit.
### Removing a bank account should not be allowed once it has been used, for both ForeignKey association reasons and Accounting reasons.
### But should we want it, Remove can just be an anchor GET route that deletes the object and redirects to dashboard or '/accounts'.
### -Will



################
### EXPENSES ### # Basically same as Accounts, I think -Will
################
def all_expense(request): #get
    pass

def add_expense(request): #get
    pass

def add_expense_processing(request): #post - (ex. add a new budget category: Snowboarding)
    pass

#To Do: View, Edit, Remove
###
### I know we didn't want multiple templates redirecting everywhere for UX reasons, but I think we at least need one template between View and Edit.
### Removing an expense account should not be allowed once it has been used, for both ForeignKey association reasons and Accounting reasons.
### But should we want it, Remove can just be an anchor GET route that deletes the object and redirects to dashboard or '/expenses'.
### -Will



###############
### PAYMENT ###
###############
def all_payment(request): #get
    if "user_id" not in request.session:
        return redirect('/')
    else:
        pass #real code block here

def new_payment(request): #get
    if "user_id" not in request.session:
        return redirect('/')
    else:
        pass #real code block here

def new_payment_processing(request): #please proofread and replace this comment with "#complete" -Will
    if request.method != "POST":
        return redirect('payments/new')
    else:
        ### retrieve objects ###
        expense = Expense.objects.get(name=request.POST["expense"]) # \ @Justin please match these <form><input name=""> in the html -Will
        account = Account.objects.get(name=request.POST["account"]) # / 
        user = User.objects.get(id=request.session["user_id"])
        ### create new payment object ###
        new_payment = Payment.objects.create(vendor=request.POST["vendor"], description=request.POST["description"], payment_amount=request.POST["payment_amount"], debit_exp=expense, credit_acc=account, owner=user)
        ### apply debit to expense ###
        expense.exp_balance = (expense.exp_balance + request.POST["payment_amount"]) #expense account is only ever debited -Will
        expense.objects.save()
        ### apply credit to account ###
        if account.category = "checking" or account.category = "saving":
            account.acc_balance = (account.acc_balance - request.POST["payment_amount"]) #crediting a bank account decrease balance -Will
        elif account.category = "credit_card":
            account.acc_balance = (account.acc_balance + request.POST["payment_amount"]) #crediting a credit card increase balance -Will
        # elif account.category = "venmo":
        #     if account.acc_balance > request.POST["payment_amount"]:
        #         account.acc_balance = account.acc_balance - request.POST["payment_amount"]
        #     else:
                ## venmo is tricky, because how do we know which bank account should be credited if venmo balance is insufficient?
                ## we can't store it in our Account model... do we need a new Model object table for Venmo alone...?
                ## then we would need to foreign key that new object into User and Payment and Transfer... highly inefficient.
                ## tentatively suggesting we leave venmo tracking as a postgrad idea.
                ## -Will
        account.objects.save()
        return redirect('/payments') # '/payments' or '/payments/new'? chances are bookkeeping is weekly at best and has like 15 entries to make... UX decision. -Will

#To Do: View, Edit, Remove
###
### Same concern regarding View and Edit as above account/expense scenario.
### Remove does not carry same concern as above. Is strictly necessary. @Joel Could you set up the URL.py and Views.py for remove?
### -Will



################
### TRANSFER ###
################
def all_transfer(request): #get
    if "user_id" not in request.session:
        return redirect('/')
    else:
        pass #real code block here

def new_transfer(request): #get
    if "user_id" not in request.session:
        return redirect('/')
    else:
        pass #real code block here

def new_transfer_processing(request): #please proofread and replace this comment with "#complete" -Will
    if request.method != "POST":
        return redirect('/transfers/new')
    else:
        ### retrieve objects ###
        acc_to_debit = Account.objects.get(name=request.POST["debit_acc"])   # \ @Justin please match these <form><input name=""> in the html -Will
        acc_to_credit = Account.objects.get(name=request.POST["credit_acc"]) # / Lowkey really tricky though, lets please discuss
        owner = User.objects.get(id=request.session["user_id"])
        ### create new transfer object ###
        new_transfer = Transfer.objects.create(vendor=request.POST["vendor"], description=request.POST["description"], transfer_amount=request.POST["transfer_amount"], debit_acc=acc_to_debit, credit_acc=acc_to_credit)
        ### apply debit to debit acc ###
        acc_to_debit.acc_balance = (acc_to_debit.acc_balance + request.POST["transfer_amount"])
        acc_to_debit.objects.save()
        ### apply credit to credit acc ###
        acc_to_credit.acc_balance = (acc_to_credit.acc_balance - request.POST["transfer_amount"])
        acc_to_credit.objects.save()
        return redirect('/transfers') # '/transfers' or '/transfers/new'? chances are bookkeeping is weekly at best and has like 15 entries to make... UX decision. -Will

#To Do: View, Edit, Remove
###
### Same concern regarding View and Edit as above account/expense scenario.
### Remove does not carry same concern as above. Is strictly necessary. @Joel Could you set up the URL.py and Views.py for remove?
### -Will



###########
### END ###
###########