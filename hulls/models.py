from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

class Hull(core_models.TimeStampedModel):

    """ Hull Model Definition """

    name = models.CharField(max_length=140)
    no = models.IntegerField()
    country = CountryField()
    description = models.TextField()
    price = models.IntegerField()
    delivery_date = models.DateField()
    owner = models.ForeignKey(
        "owners.Owner", on_delete=models.CASCADE, related_name="hulls"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-pk"]

