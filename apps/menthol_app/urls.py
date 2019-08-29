from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'^expenses$', views.all_expense),
    url(r'^expenses/new$', views.add_expense),
    url(r'^expenses/processing$', views.add_expense_processing),
    url(r'^accounts$', views.all_account),
    url(r'^accounts/new$', views.add_account),
    url(r'^accounts/processing$', views.add_account_processing),
    url(r'^transfers$', views.all_transfer),
    url(r'^transfers/new$', views.new_transfer),
    url(r'^transfers/processing$', views.new_transfer_processing),
    url(r'^payments$', views.all_payment),
    url(r'^payments/new$', views.new_payment),
    url(r'^payments/processing$', views.new_payment_processing),

]