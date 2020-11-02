from rest_framework.viewsets import ModelViewSet
from .models import Owner
from .serializers import OwnerSerializer


class OwnersViewSet(ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
