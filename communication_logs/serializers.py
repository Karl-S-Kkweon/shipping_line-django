from rest_framework import serializers
from .models import communication_logs
from hull_report.serializers import HullReportSerializer


class CommunicationLogsSerializer(serializers.ModelSerializer):

    hull_report = HullReportSerializer() #many=True

    class Meta:
        model = communication_logs
        exclude = ("created", "updated")
