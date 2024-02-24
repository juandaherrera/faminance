from django.views.generic import ListView

from apps.utils.functions import breadcrumbs_format

from .models import Account, AccountType


class AccountTypeListView(ListView):
    model = AccountType
    template_name = 'account_type_list.html'
    breadcrumbs = (
        ('Home', 'core:index'),
        ('Tipos de Cuenta', None),
    )
    info = {'header': {'title': 'Tipos de Cuenta'}}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = breadcrumbs_format(self.breadcrumbs)
        context['info'] = self.info
        return context


class AccountListView(ListView):
    model = Account
    template_name = 'account_list.html'
    breadcrumbs = (
        ('Home', 'core:index'),
        ('Cuentas', None),
    )
    info = {'header': {'title': 'Cuentas'}}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = breadcrumbs_format(self.breadcrumbs)
        context['info'] = self.info
        return context
