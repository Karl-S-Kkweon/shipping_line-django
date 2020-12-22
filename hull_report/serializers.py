from rest_framework import serializers
from .models import HullReport
from hulls.serializers import HullSerializer


class HullReportSerializer(serializers.ModelSerializer):

    hulls = HullSerializer(one=True)

    class Meta:
        model = HullReport
        exclude = ("created", "updated")
