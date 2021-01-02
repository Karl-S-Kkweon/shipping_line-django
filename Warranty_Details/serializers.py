from rest_framework import serializers
from .models import Warranty_Details
from hull_report.serializers import HullReportSerializer


class WarrantyDetailsSerializer(serializers.ModelSerializer):

    hull_report = HullReportSerializer() #many=True

    class Meta:
        model = Warranty_Details
        exclude = ("created", "updated")
