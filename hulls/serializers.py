from rest_framework import serializers
from .models import Hull
from owners.serializers import OwnerSerializer


class HullSerializer(serializers.ModelSerializer):

    owner = OwnerSerializer()

    class Meta:
        model = Hull
        exclude = ("created", "updated")
