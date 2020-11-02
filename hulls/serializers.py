from rest_framework import serializers
from .models import Hull
from owners.serializers import OwnerSerializer


class HullSerializer(serializers.ModelSerializer):

    owners = OwnerSerializer(many=True)

    class Meta:
        model = Hull
        exclude = ("created", "updated")
