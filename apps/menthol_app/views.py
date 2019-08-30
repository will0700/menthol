from django.shortcuts import render, redirect
from apps.login_reg.models import *
from .models import *



#################
### DASHBOARD ###
#################
def dashboard(request): #in progress
    if "user_id" not in request.session:
        return redirect("/")
    else:
        user = User.objects.get(id=request.session["user_id"])
        # all_payments = Payment.objects.filter(owner=user).values_list("created_at", "vendor", "description", "amount")
        # all_transfers = Transfer.objects.filter(owner=user).values_list("created_at", "vendor", "description", "amount")
        # all_transactions = all_payments.union(all_transfers)
        all_accounts = Account.objects.filter(owner=user)
        all_expenses = Expense.objects.filter(owner=user)
        all_payments = Payment.objects.filter(owner=user)
        all_transfers = Transfer.objects.filter(owner=user)
        all_percentages = {}
        for expense in all_expenses:
            all_percentages[expense.id] = expense.exp_balance/expense.budget
        context = {
            "user": user,
            "all_accounts": all_accounts,
            "all_expenses": all_expenses,
            "all_payments": all_payments,
            "all_transfers": all_transfers,
            # "all_transactions": all_transactions,
            "all_percentages": all_percentages,
        }
        return render(request, "menthol_app/dashboard.html", context)

################
### ACCOUNTS ###
################
def all_account(request): #complete, not tested
    if "user_id" not in request.session:
        return redirect("/")
    else:
        user = User.objects.get(id=request.session["user_id"])
        all_accounts = Account.objects.filter(owner=user)
        all_expenses = Expense.objects.filter(owner=user)
        all_percentages = {}
        for expense in all_expenses:
            all_percentages[expense.id] = expense.exp_balance/expense.budget
        context = {
            "user": user,
            "all_accounts": all_accounts,
            "all_expenses": all_expenses,
            "all_percentages": all_percentages,
        }
        return render(request, "menthol_app/all_account.html", context)

def add_account(request): #complete, not tested
    if "user_id" not in request.session:
        return redirect("/")
    else:
        user = User.objects.get(id=request.session["user_id"])
        context = {
            "user": user,
        }
        return render(request, "/menthol_app/all_account.html", context)

def add_account_processing(request): #complete, not tested
    if request.method != "POST":
        return redirect("/accounts/new")
    form = request.POST
    user = User.objects.get(id = request.session["user_id"])
    new_account = Account.objects.create(name=form["name"], acc_balance=form["acc_balance"], category=form["category"], owner=user)
    return redirect("/accounts")

def view_account(request, acc_id): ### DO NOT USE ###
    if "user_id" not in request.session:
        return redirect("/")
    else:
        user = User.objects.get(id=request.session["user_id"])
        account = Account.objects.get(id=acc_id)
        if account.owner != user:
            return redirect("/accounts")
        else:
            context = {
                "user": user,
                "account": account,
            }
            return render(request, "menthol_app/view_account.html", context)

def edit_account(request, acc_id): ### DO NOT USE ###
    if "user_id" not in request.session:
        return redirect ('/')
    else:
        user = User.objects.get(id=request.session["user_id"])
        acc_to_edit = Account.objects.get(id=acc_id)
        if acc_to_edit.owner != user:
            return redirect("/accounts")
        else:
            context = {
                "user": user,
                "acc_to_edit": acc_to_edit
            }
            return render(request, "menthol_app/edit_account.html", context)

def edit_account_processing(request, acc_id): ### DO NOT USE ###
    if request.method != "POST":
        return redirect ("/edit_account")
    else:
        user = User.objects.get(id=request.session["user_id"])
        acc_to_edit = Account.objects.get(id=acc_id)
        acc_to_edit.name = request.POST["name"]
        # acc_to_edit.balance = request.POST["balance"]
        # should balance be allowed for manual edit...??? -Will
        acc_to_edit.category = request.POST["category"]
        acc_to_edit.save()
        return redirect('/accounts')

# def remove_account(request, acc_id): #complete, not tested ***DO NOT USE***
#     if "user_id" not in request.session:
#         return redirect('/')
#     else:
#         user = User.objects.get(id=request.session["user_id"])
#         acc_to_remove = Account.objects.get(id=acc_id)
#         if acc_to_remove.owner != user:
#             return redirect("/accounts")
#         else:
#             acc_to_remove.objects.delete()
#             return redirect("/accounts")
### Removing a bank account should not be allowed once it has been used, for both ForeignKey association reasons and Accounting reasons.
### Not sure how to test if ForeignKey relationship exists though... Should we completely disable?
### -Will



################
### EXPENSES ###
################
def all_expense(request): #complete, not tested
    if "user_id" not in request.session:
        return redirect("/")
    else:
        user = User.objects.get(id=request.session["user_id"])
        all_expenses = Expense.objects.filter(owner=user)
        context = {
            "user": user,
            "all_expenses": all_expenses,
        }
        return render(request, "menthol_app/all_account.html", context)

def add_expense(request): #complete, not tested
    if "user_id" not in request.session:
        return redirect("/")
    else:
        user = User.objects.get(id=request.session["user_id"])
        context = {
            "user": user,
        }
        return render(request, "/menthol_app/all_account.html", context)

def add_expense_processing(request): #complete, not tested
    if request.method != "POST":
        return redirect("/accounts/new")
    form = request.POST
    user = User.objects.get(id = request.session["user_id"])
    new_expense = Expense.objects.create(name=form["name"], exp_balance=0, budget=form["budget"], owner=user)
    return redirect("/accounts")

def view_expense(request, exp_id): ### DO NOT USE ###
    if "user_id" not in request.session:
        return redirect("/")
    else:
        user = User.objects.get(id=request.session["user_id"])
        expense = Expense.objects.get(id=acc_id)
        if expense.owner != user:
            return redirect("/accounts")
        else:
            context = {
                "user": user,
                "expense": expense,
            }
            return render(request, "menthol_app/view_expense.html", context)

def edit_expense(request, exp_id): ### DO NOT USE ###
    if "user_id" not in request.session:
        return redirect ('/')
    else:
        user = User.objects.get(id=request.session["user_id"])
        exp_to_edit = Expense.objects.get(id=exp_id)
        if exp_to_edit.owner != user:
            return redirect("/expenses")
        else:
            context = {
                "user": user,
                "exp_to_edit": exp_to_edit
            }
            return render(request, "menthol_app/edit_expense.html", context)

def edit_expense_processing(request, acc_id): ### DO NOT USE ###
    if request.method != "POST":
        return redirect ("/edit_expense")
    else:
        user = User.objects.get(id=request.session["user_id"])
        exp_to_edit = Expense.objects.get(id=exp_id)
        exp_to_edit.name = request.POST["name"]
        # exp_to_edit.balance = request.POST["balance"]
        # should balance be allowed for manual edit...??? -Will
        exp_to_edit.category = request.POST["category"]
        exp_to_edit.save()
        return redirect('/expenses')

def remove_expense(request, exp_id): #to do
    pass
### Removing an expense account should not be allowed once it has been used, for both ForeignKey association reasons and Accounting reasons.
### But should we want it, Remove can just be an anchor GET route that deletes the object and redirects to dashboard or "/expenses".
### -Will



###############
### PAYMENT ###
###############
def all_payment(request): #complete, not tested
    if "user_id" not in request.session:
        return redirect("/")
    else:
        user = User.objects.get(id=request.session["user_id"])
        all_payments = Payment.objects.filter(owner=user)
        all_transfers = Transfer.objects.filter(owner=user)
        all_accounts = Account.objects.filter(owner=user)
        all_expenses = Expense.objects.filter(owner=user)
        context = {
            "user": user,
            "all_accounts": all_accounts,
            "all_expenses": all_expenses,
            "all_payments": all_payments,
            "all_transfers": all_transfers,
        }
        return render(request, "menthol_app/all_transfer.html", context)


def new_payment(request): #complete, not tested
    if "user_id" not in request.session:
        return redirect("/")
    else:
        user = User.objects.get(id=request.session["user_id"])
        context = {
            "user": user,
        }
        return render(request, "menthol_app/all_transfer.html", context)

def new_payment_processing(request): #complete, not tested
    if request.method != "POST":
        return redirect("payments/new")
    else:
        ### retrieve objects ###
        expense = Expense.objects.get(name=request.POST["expense"]) # \ @Justin please match these <form><input name=""> in the html -Will
        account = Account.objects.get(name=request.POST["account"]) # / 
        user = User.objects.get(id=request.session["user_id"])
        ### create new payment object ###
        new_payment = Payment.objects.create(vendor=request.POST["vendor"], description=request.POST["description"], amount=request.POST["amount"], debit_exp=expense, credit_acc=account, owner=user)
        ### apply debit to expense ###
        expense.exp_balance = (expense.exp_balance + request.POST["amount"]) #expense account is only ever debited -Will
        expense.objects.save()
        ### apply credit to account ###
        if account.category == "checking" or account.category == "saving":
            account.acc_balance = (account.acc_balance - request.POST["amount"]) #crediting a bank account decrease balance -Will
        elif account.category == "credit_card":
            account.acc_balance = (account.acc_balance + request.POST["amount"]) #crediting a credit card increase balance -Will
        # elif account.category = "venmo":
        #     if account.acc_balance > request.POST["amount"]:
        #         account.acc_balance = account.acc_balance - request.POST["amount"]
        #     else:
                ## venmo is tricky, because how do we know which bank account should be credited if venmo balance is insufficient?
                ## we can"t store it in our Account model... do we need a new Model object table for Venmo alone...?
                ## then we would need to foreign key that new object into User and Payment and Transfer... highly inefficient.
                ## tentatively suggesting we leave venmo tracking as a postgrad idea.
                ## -Will
        account.objects.save()
        return redirect("/payments")

def view_payment(request, pmt_id): #to do
    pass

def edit_payment(request, pmt_id): #to do
    pass

def remove_payment(request, pmt_id): #to do
    pass



################
### TRANSFER ###
################
def all_transfer(request): #complete, not tested
    if "user_id" not in request.session:
        return redirect("/")
    else:
        user = User.objects.get(id=request.session["user_id"])
        all_transfers = Transfer.objects.filter(owner=user)
        context = {
            "user": user,
            "all_transfers": all_transfers,
        }
        return render(request, "menthol_app/all_transfer.html", context)

def new_transfer(request): #complete, not tested
    if "user_id" not in request.session:
        return redirect("/")
    else:
        user = User.objects.get(id=request.session["user_id"])
        context = {
            "user": user,
        }
        return render(request, "menthol_app/all_transfer.html", context)

def new_transfer_processing(request): #complete, not tested
    if request.method != "POST":
        return redirect("/transfers/new")
    else:
        ### retrieve objects ###
        acc_to_debit = Account.objects.get(name=request.POST["debit_acc"])   # \ @Justin please match these <form><input name=""> in the html -Will
        acc_to_credit = Account.objects.get(name=request.POST["credit_acc"]) # / Lowkey really tricky though, lets please discuss
        owner = User.objects.get(id=request.session["user_id"])
        ### create new transfer object ###
        new_transfer = Transfer.objects.create(vendor=request.POST["vendor"], description=request.POST["description"], amount=request.POST["amount"], debit_acc=acc_to_debit, credit_acc=acc_to_credit)
        ### apply debit to debit acc ###
        acc_to_debit.acc_balance = (acc_to_debit.acc_balance + request.POST["amount"])
        acc_to_debit.objects.save()
        ### apply credit to credit acc ###
        acc_to_credit.acc_balance = (acc_to_credit.acc_balance - request.POST["amount"])
        acc_to_credit.objects.save()
        return redirect("/transfers")

def view_transfer(request, xfer_id): #to do
    pass

def edit_transfer(request, xfer_id): #to do
    pass

def remove_transfer(request, xfer_id): #to do
    pass



###########
### END ###
###########