from rest_framework.viewsets import ModelViewSet
from .models import Warranty_Details
from .serializers import WarrantyDetailsSerializer


class ListWarrantyDetailsView(ModelViewSet):

    queryset = Warranty_Details.objects.all()
    serializer_class = WarrantyDetailsSerializer
