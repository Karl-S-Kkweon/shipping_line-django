from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Warranty_Details)
class WarrantyDetailsAdmin(admin.ModelAdmin):

    """ Custom WarrantyDetails Admin """

    list_display = (
        "report_number",
        #"responsibility",
        "status",
        "section",
        "importance",
        "remark",
        "return_product",
        "internal_report",
        "compensation",
        "unit",
        "report_summary",
        "requested_action",
    )

    list_filter = ("status",)