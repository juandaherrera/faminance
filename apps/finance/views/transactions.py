from django.urls import reverse_lazy

from apps.utils.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseListView,
    BaseUpdateView,
)

from ..forms import AccountForm
from ..models import Transaction


class TransactionListView(BaseListView):
    model = Transaction
    template_name = 'transactions/transaction_list.html'
    breadcrumbs = (
        ('Home', 'core:index'),
        ('Transacciones', None),
    )

    def get_queryset(self):
        return Transaction.objects.filter(account___deleted=False).order_by('-date')


"""
class AccountCreateView(BaseCreateView):
    model = Account
    form_class = AccountForm
    success_url = reverse_lazy('finance:account-list')
    template_name = 'accounts/account_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountUpdateView(BaseUpdateView):
    model = Account
    form_class = AccountForm
    success_url = reverse_lazy('finance:account-list')
    template_name = "accounts/account_form.html"


class AccountDeleteView(BaseDeleteView):
    model = Account
    success_url = reverse_lazy('finance:account-list')
"""
