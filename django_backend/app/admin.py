from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
from .models import *

"""add anime inlines for related models to reverse lookup easilier"""
class AnimeInline(admin.TabularInline):
    model = None  # placeholder to be set dynamically later in loop
    extra = 0
    verbose_name = "Anime"
    verbose_name_plural = "Animes"

for model in [Theme, Genre, Studio, Producer]:
    through_model = Anime._meta.get_field(model.__name__.lower() + 's').remote_field.through

    # custom inline class for each through model
    inline = type(f'{model.__name__}AnimeInline', (AnimeInline,), {
        'model': through_model,
    })

    # then a custom admin class for each related model
    admin_class = type(f'{model.__name__}Admin', (admin.ModelAdmin,), {
        'inlines': [inline],
    })

    # register
    admin.site.register(model, admin_class)

# and for the rest unrelated models
for model in apps.get_app_config('app').get_models():
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass

