from rest_framework import serializers
from .models import relevant_groups
from hull_report.serializers import HullReportSerializer


class RelevantGroupsSerializer(serializers.ModelSerializer):

    Hull_Report = HullReportSerializer() #many=True

    class Meta:
        model = relevant_groups
        exclude = ("created", "updated")
