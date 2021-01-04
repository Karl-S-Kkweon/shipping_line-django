from django.db import models
from core import models as core_models
from hull_report import models as hull_report_models

# Create your models here.
class relevant_groups(core_models.TimeStampedModel):
    report_number = models.ForeignKey(hull_report_models.Hull_Report, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    item = models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return str(self.report_number)

    class Meta:
        ordering = ["-pk"]