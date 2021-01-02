from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.communication_logs)
class CommunicationLogsAdmin(admin.ModelAdmin):

    """ Custom CommunicationLogs Admin """

    list_display = (
        "report_number",
        "contact_date",
        "description"
    )
    
    list_filter = ("report_number",)