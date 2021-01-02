from rest_framework.viewsets import ModelViewSet
from .models import communication_logs
from .serializers import CommunicationLogsSerializer


class ListCommunicationLogsView(ModelViewSet):

    queryset = communication_logs.objects.all()
    serializer_class = CommunicationLogsSerializer
