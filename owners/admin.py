from django.contrib import admin
from . import models


@admin.register(models.Owner)
class OwnerAdmin(admin.ModelAdmin):

    """ Custom Owner Admin """

    list_display = ("name", "is_supervisor")

    list_filter = ("is_supervisor",)
