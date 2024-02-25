from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from apps.utils.functions import breadcrumbs_format

from .forms import AccountForm
from .models import Account, AccountType


class AccountTypeListView(ListView):
    model = AccountType
    template_name = 'account_type_list.html'
    breadcrumbs = (
        ('Home', 'core:index'),
        ('Tipos de Cuenta', None),
    )
    info = {
        'header': {'title': 'Tipos de Cuenta'},
        'others': {'create_button': 'Agregar Tipo de Cuenta'},
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = breadcrumbs_format(self.breadcrumbs)
        context['info'] = self.info
        return context


# TO_DO crear modelo pydantic de los campos pasados como contexto
class AccountListView(ListView):
    model = Account
    template_name = 'account_list.html'
    breadcrumbs = (
        ('Home', 'core:index'),
        ('Cuentas', None),
    )
    info = {
        'header': {'title': 'Cuentas'},
        'model': {'name': Account._meta.verbose_name},
        'others': {
            'create_button': 'Agregar Cuenta',
            'create_url': reverse_lazy('finance:account-create'),
        },
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = breadcrumbs_format(self.breadcrumbs)
        context['info'] = self.info
        return context


class AccountCreateView(CreateView):
    model = Account
    form_class = AccountForm
    success_url = reverse_lazy('finance:account-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_template_names(self):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return ['account_form.html']
        else:
            return ['']
