from django.contrib import admin
from . import models


@admin.register(models.Owner)
class HullAdmin(admin.ModelAdmin):

    pass
