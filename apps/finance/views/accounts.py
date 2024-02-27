from django.db.models import Max
from django.urls import reverse_lazy

from apps.utils.views import (
    BaseCreateView,
    BaseDeleteView,
    BaseListView,
    BaseUpdateView,
)

from ..forms import AccountForm
from ..models import Account, AccountType


class AccountTypeListView(BaseListView):
    model = AccountType
    template_name = 'accounts/account_type_list.html'
    breadcrumbs = (
        ('Home', 'core:index'),
        ('Tipos de Cuenta', None),
    )


class AccountListView(BaseListView):
    model = Account
    template_name = 'accounts/account_list.html'
    breadcrumbs = (
        ('Home', 'core:index'),
        ('Cuentas', None),
    )

    def get_queryset(self):
        return Account.objects.annotate(last_transaction_date=Max('transaction__date')).order_by(
            '-last_transaction_date'
        )


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
