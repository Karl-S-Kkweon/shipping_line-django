from django.db import models
from core import models as core_models
from hull_report import models as hull_report_models
# from enum import Enum
# from django.utils.translation import gettext_lazy as _

class Warranty_Details(core_models.TimeStampedModel):

    class YesNo(models.TextChoices):
        YES = 1,
        NO = 0

    class Status(models.TextChoices):
        OPEN = 1,
        ITEM_READY = 2,
        ITEM_SHIPPED = 3,
        COMPENSATION = 4,
        CLOSE = 5

    class Sections(models.TextChoices):
        HULL = 1,
        MACHINERY = 2,
        PAINTING = 3,
        ACCOMMODATION = 4, 
        DESIGN = 5,
        MANAGEMENT = 6,


    class Importances(models.TextChoices):
        AA = 'Critical',
        BB = 'Urgent',
        CC = 'Moderate',
        DD = 'Minor'
    
    class Remarks(models.TextChoices):
        WMR = 'Wating Maker Reply',
        WYR = 'Wating Yard Reply',
        WVR = 'Wating Vessel Reply',
        ITR = 'Item Ready'

    class MonetaryUnits(models.TextChoices):
        USD = 1,
        CAD = 2,
        EUR = 3,
        KRW = 4

    """ Warranty_Details Model Definition """
    # hulls = models.ForeignKey(hull_report_models.Hull_Report, on_delete=models.CASCADE)
    report_number = models.ForeignKey(hull_report_models.Hull_Report, on_delete=models.CASCADE)
    # responsibility = models.ForeignKey(hull_report_models.Hull_Report, on_delete=models.CASCADE)
    
    status = models.CharField(
        max_length=12,
        choices=Status.choices,
        default=Status.OPEN
    )

    return_product = models.CharField(
        max_length=3,
        choices=YesNo.choices,
        default=YesNo.NO
    )

    internal_report = models.CharField(
        max_length=3,
        choices=YesNo.choices,
        default=YesNo.NO
    )

    section = models.CharField(
        max_length=15,
        choices=Sections.choices,
        #default=Section.OPEN
    )
    
    importance = models.CharField(
        max_length=8,
        choices=Importances.choices,
        default=Importances.DD
    )

    remark = models.CharField(
        max_length=20,
        choices=Remarks.choices,
        default=Remarks.WMR
    )

    compensation = models.DecimalField(decimal_places = 2, max_digits = 6, default = 0)
    
    unit = models.CharField(
        max_length=3,
        choices=MonetaryUnits.choices,
        blank=True, null=True
    )
    
    report_summary = models.TextField(blank=True, null=True) #max_length=500, blank=True, null=True

    requested_action = models.TextField(blank=True, null=True) #max_length=250, blank=True, null=True

    def __str__(self):
        return str(self.report_number)

    class Meta:
        ordering = ["-pk"]



