from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.manufacturers)
class ManufacturersAdmin(admin.ModelAdmin):

    """ Custom WarrantyDetails Admin """

    list_display = (
        "name",
        "product"
    )

    list_filter = ("name",)