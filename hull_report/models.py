from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from hulls import models as hull_models

class Hull_Report(core_models.TimeStampedModel):

    """ Hull_Report Model Definition """
    hulls = models.ForeignKey(hull_models.Hull, on_delete=models.CASCADE)
    report_number = models.IntegerField()    
    subject = models.CharField(max_length=120)
    equipment = models.CharField(max_length=120)
    manufacturer = models.CharField(max_length=120)
    drawing_number = models.CharField(max_length=120)
    type_name = models.CharField(max_length=120)
    description_damage = models.TextField()
    occurrence_date = models.DateField()
    putative_cause = models.CharField(max_length=120)
    # repair_works_done = models.ENUM?
    vessel_comment = models.TextField()
    # vessel_files =
    # yard_files =

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ["-pk"]
