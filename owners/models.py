from django.db import models
from core import models as core_models


class Owner(core_models.TimeStampedModel):

    """ Owner Model Definition """

    name = models.CharField(max_length=120, default="")
    is_supervisor = models.BooleanField(default=False)

    def count_hulls(self):
        return self.hulls.count()

    count_hulls.short_description = "Number of Hulls"

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-pk"]
