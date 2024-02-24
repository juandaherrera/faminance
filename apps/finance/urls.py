from django.urls import path

from .views import AccountListView, AccountTypeListView

app_name = 'finance'

urlpatterns = [
    path(
        'account-type', AccountTypeListView.as_view(), name='account-type-list'
    ),
    path('account', AccountListView.as_view(), name='account-list'),
]
