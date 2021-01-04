from django.db import models
from core import models as core_models
from hull_report import models as hull_report_models

# Create your models here.
class communication_logs(core_models.TimeStampedModel):
    report_number = models.ForeignKey(hull_report_models.Hull_Report, on_delete=models.CASCADE)
    contact_date = models.DateField()
    description = models.TextField()
    
    def __str__(self):
        return str(self.report_number)

    class Meta:
        ordering = ["-pk"]