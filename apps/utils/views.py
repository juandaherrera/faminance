from typing import List, Tuple, Union

from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.utils.functions import breadcrumbs_format


class ContextMixin:

    info = {}
    breadcrumbs: List[Tuple[str, Union[str, None]]] = ()

    def get_context_extra_info(self) -> None:
        self.info['model'] = {
            'verbose_name': self.model._meta.verbose_name,
            'verbose_name_plural': self.model._meta.verbose_name_plural,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.get_context_extra_info()
        context['info'] = self.info
        context['breadcrumbs'] = breadcrumbs_format(self.breadcrumbs)
        return context


class BaseListView(ContextMixin, ListView):
    pass


class BaseCreateView(ContextMixin, CreateView):
    pass


class BaseUpdateView(ContextMixin, UpdateView):
    pass


class BaseDeleteView(ContextMixin, DeleteView):
    pass
