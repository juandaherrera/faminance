from django.urls import reverse_lazy

from apps.utils.views import BaseCreateView, BaseListView, BaseUpdateView

from .forms import AccountForm
from .models import Account, AccountType


class AccountTypeListView(BaseListView):
    model = AccountType
    template_name = 'account_type_list.html'
    breadcrumbs = (
        ('Home', 'core:index'),
        ('Tipos de Cuenta', None),
    )


class AccountListView(BaseListView):
    model = Account
    template_name = 'account_list.html'
    breadcrumbs = (
        ('Home', 'core:index'),
        ('Cuentas', None),
    )


class AccountCreateView(BaseCreateView):
    model = Account
    form_class = AccountForm
    success_url = reverse_lazy('finance:account-list')
    template_name = "account_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountUpdateView(BaseUpdateView):
    model = Account
    form_class = AccountForm
    success_url = reverse_lazy('finance:account-list')
    template_name = "account_form.html"
