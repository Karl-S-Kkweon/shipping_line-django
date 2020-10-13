from django.contrib import admin
from . import models


@admin.register(models.Owner)
class OwnerAdmin(admin.ModelAdmin):

    pass
