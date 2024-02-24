from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Obtén el contexto existente de la clase base
        context = super().get_context_data(**kwargs)
        # Genera los breadcrumbs
        context['breadcrumbs'] = [
            {'name': 'Home', 'url': '/'},
        ]
        return context
