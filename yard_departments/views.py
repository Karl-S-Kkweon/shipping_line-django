from rest_framework.viewsets import ModelViewSet
from .models import yard_departments
from .serializers import YardDepartmentsSerializer


class ListYardDepartmentsView(ModelViewSet):

    queryset = yard_departments.objects.all()
    serializer_class = YardDepartmentsSerializer
