from rest_framework.viewsets import ModelViewSet
from .models import Hull_Report
from .serializers import HullReportSerializer


class ListHullReportsView(ModelViewSet):

    queryset = Hull_Report.objects.all()
    serializer_class = HullReportSerializer
