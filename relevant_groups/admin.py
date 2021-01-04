from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.relevant_groups)
class RelevantGroupsAdmin(admin.ModelAdmin):
    
    list_display = (
        "report_number",
        "name",
        "item"
    )

    list_filter = ("report_number",)
