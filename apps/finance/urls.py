from django.urls import path

from .views import (
    AccountCreateView,
    AccountListView,
    AccountTypeListView,
    AccountUpdateView,
)

app_name = 'finance'

urlpatterns = [
    path('account-type', AccountTypeListView.as_view(), name='account-type-list'),
    path('account', AccountListView.as_view(), name='account-list'),
    path('account/modal/create', AccountCreateView.as_view(), name='account-create-modal'),
    path(
        'account/modal/update/<int:pk>', AccountUpdateView.as_view(), name='account-update-modal'
    ),
]
