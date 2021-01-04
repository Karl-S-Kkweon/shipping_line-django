from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Hull_Report)
class HullReportAdmin(admin.ModelAdmin):

    """ Custom HullReport Admin """

    list_display = (
        "report_number",
        "hulls",
        "subject",
        "equipment",
        "occurrence_date",
    )

    list_filter = ("report_number",)
