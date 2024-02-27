from django.urls import path

from . import views

app_name = 'finance'

urlpatterns = [
    path('account-type', views.AccountTypeListView.as_view(), name='account-type-list'),
    # ----------------------- Accounts -----------------------
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
    # ----------------------- Transactions -----------------------
    path('transactions', views.TransactionListView.as_view(), name='transaction-list'),
    path(
        'transactions/modal/create',
        views.TransactionCreateView.as_view(),
        name='transaction-create-modal',
    ),
    path(
        'transactions/modal/update/<int:pk>',
        views.TransactionUpdateView.as_view(),
        name='transaction-update-modal',
    ),
    path(
        'account/modal/delete/<int:pk>',
        views.TransactionDeleteView.as_view(),
        name='transaction-delete-modal',
    ),
]
