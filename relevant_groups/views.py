from rest_framework.viewsets import ModelViewSet
from .models import relevant_groups
from .serializers import RelevantGroupsSerializer


class ListRelevantGroupsView(ModelViewSet):
    queryset = relevant_groups.objects.all()
    serializer_class = RelevantGroupsSerializer
