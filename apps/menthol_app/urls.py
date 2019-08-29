from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^expenses$', views.all_expense),
    url(r'^expenses/new$', views.add_new_expense),
    url(r'^expenses/processing$', views.add_expense_processing),
    url(r'^accounts$', views.all_account),
    url(r'^accounts/new$', views.add_new_account),
    url(r'^accounts/processing$', views.add_account_processing),
    url(r'^transfers$', views.all_transfer),
    url(r'^transfers/new$', views.add_new_transfer),
    url(r'^transfers/processing$', views.add_transfer_processing),
    url(r'^payments$', views.all_payment),
    url(r'^payments/new$', views.add_new_payment),
    url(r'^payments/processing$', views.add_payment_processing),

]