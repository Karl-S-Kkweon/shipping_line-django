from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# Create your models here.
class manufacturers(core_models.TimeStampedModel):
    name = models.CharField(max_length=50,)
    product = models.CharField(max_length=25,blank=True)
    company_registry = CountryField()

    def __str__(self):
        return (self.name)

    class Meta:
        ordering = ["-pk"]