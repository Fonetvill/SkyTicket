# from django.contrib import admin
# from .models import Flights
# # Register your models here.
#
# admin.site.register(Flights)
#
from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('main')
for model_name, model in app.models.items():
    admin.site.register(model)