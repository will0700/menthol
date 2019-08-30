from django.conf.urls import url
from . import views

urlpatterns = [
    #dashboard#
    url(r'^dashboard$', views.dashboard),
    #expenses#
    url(r'^expenses$', views.all_expense),
    url(r'^expenses/add$', views.add_expense),
    url(r'^expenses/add/processing$', views.add_expense_processing),
    # url(r'^expenses/view/(?P<exp_id>\d+)$', views.view_expense),
    # url(r'^expenses/edit/(?P<exp_id>\d+)$', views.edit_expense),
    # url(r'^expenses/edit/(?P<exp_id>\d+)/processing$', views.edit_expense_processing),
    #url(r'^expenses/remove/(?P<exp_id>\d+)$', views.remove_expense),
    #accounts#
    url(r'^accounts$', views.all_account),
    url(r'^accounts/add$', views.add_account),
    url(r'^accounts/add/processing$', views.add_account_processing),
    # url(r'^accounts/view/(?P<acc_id>\d+)$', views.view_account),
    # url(r'^accounts/edit/(?P<acc_id>\d+)$', views.edit_account),
    # url(r'^accounts/edit/(?P<acc_id>\d+)/processing$', views.edit_account_processing),
    #url(r'^accounts/remove/(?P<acc_id>\d+)$', views.remove_account),
    #transfers#
    url(r'^transfers$', views.all_transfer),
    url(r'^transfers/new$', views.new_transfer),
    url(r'^transfers/processing$', views.new_transfer_processing),
    # url(r'^transfers/view/(?P<xfer_id>\d+)$', views.view_transfer),
    # url(r'^transfers/edit/(?P<xfer_id>\d+)$', views.edit_transfer),
    # url(r'^transfers/remove/(?P<xfer_id>\d+)$', views.remove_transfer),
    #payments#
    url(r'^payments$', views.all_payment),
    url(r'^payments/new$', views.new_payment),
    url(r'^payments/processing$', views.new_payment_processing),
    # url(r'^payments/view/(?P<pmt_id>\d+)$', views.view_payment),
    # url(r'^payments/edit/(?P<pmt_id>\d+)$', views.edit_payment),
    # url(r'^payments/remove/(?P<pmt_id>\d+)$', views.remove_payment),
]