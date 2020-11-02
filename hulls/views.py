from rest_framework.generics import ListAPIView
from .models import Hull
from .serializers import HullSerializer


class ListHullsView(ListAPIView):

    queryset = Hull.objects.all()
    serializer_class = HullSerializer
