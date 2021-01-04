from rest_framework import serializers
from .models import manufacturers

class manufacturersSerializer(serializers.ModelSerializer):

    class Meta:
        model = manufacturers
        exclude = ("created", "updated")
