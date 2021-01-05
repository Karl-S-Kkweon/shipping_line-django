from rest_framework.viewsets import ModelViewSet
from .models import Owner
from .serializers import OwnerSerializer
from django.views.generic import ListView, DetailView


class OwnersViewSet(ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class OwnerList(ListView):

    """ OwnerList Definition """

    model = Owner
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "owners"


class OwnerDetail(DetailView):

    """ OwnerDetail Definition """

    model = Owner
