from django.db import models
from core import models as core_models

# Create your models here.
class yard_departments(core_models.TimeStampedModel):
    name = models.CharField(max_length=50,)

    def __str__(self):
        return (self.name)

    class Meta:
        ordering = ["-pk"]
    