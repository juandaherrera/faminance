from django.contrib import admin

from .models import MODELS_LIST

for model in MODELS_LIST:
    admin.site.register(model)
