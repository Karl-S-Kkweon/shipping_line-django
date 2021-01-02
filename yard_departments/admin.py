from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.yard_departments)
class YardDepartmentsAdmin(admin.ModelAdmin):

    """ Custom YardDepartments Admin """

    list_display = (
        "name",
    )

    list_filter = ("name",)