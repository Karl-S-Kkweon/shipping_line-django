from rest_framework.viewsets import ModelViewSet
from .models import Hull
from .serializers import HullSerializer


class ListHullsView(ModelViewSet):

    queryset = Hull.objects.all()
    serializer_class = HullSerializer
