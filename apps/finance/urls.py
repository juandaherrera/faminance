from django.urls import path

from . import views

app_name = 'finance'

urlpatterns = [
    path('account-type', views.AccountTypeListView.as_view(), name='account-type-list'),
    path('accounts', views.AccountListView.as_view(), name='account-list'),
    path('account/modal/create', views.AccountCreateView.as_view(), name='account-create-modal'),
    path(
        'accounts/modal/update/<int:pk>',
        views.AccountUpdateView.as_view(),
        name='account-update-modal',
    ),
    path(
        'account/modal/delete/<int:pk>',
        views.AccountDeleteView.as_view(),
        name='account-delete-modal',
    ),
    # Transactions
    path('transactions', views.TransactionListView.as_view(), name='transaction-list'),
]
