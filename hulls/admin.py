from django.contrib import admin
from . import models


@admin.register(models.Hull)
class HullAdmin(admin.ModelAdmin):

    """ Custom Hull Admin """

    list_display = (
        "name",
        "no",
        "country",
        "description",
        "price",
        "delivery_date",
        "owner"
    )

    list_filter = ("country",)
