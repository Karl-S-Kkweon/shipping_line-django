from rest_framework import serializers
from .models import yard_departments

class YardDepartmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = yard_departments
        exclude = ("created", "updated")
