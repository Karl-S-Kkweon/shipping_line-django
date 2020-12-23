from rest_framework import serializers
from .models import Hull_Report
from hulls.serializers import HullSerializer


class HullReportSerializer(serializers.ModelSerializer):

    hulls = HullSerializer() #many=True

    class Meta:
        model = Hull_Report
        exclude = ("created", "updated")
