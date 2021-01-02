from rest_framework.viewsets import ModelViewSet
from .models import manufacturers
from .serializers import manufacturersSerializer


class ListManufacturersView(ModelViewSet):

    queryset = manufacturers.objects.all()
    serializer_class = manufacturersSerializer
