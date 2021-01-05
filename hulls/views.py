from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.core.paginator import Paginator
from .serializers import HullSerializer
from .models import Hull
from .forms import SearchForm


class ListHullsView(ModelViewSet):

    queryset = Hull.objects.all()
    serializer_class = HullSerializer


class HullList(ListView):

    """ HullList Definition """

    model = Hull
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "hulls"


class HullDetail(DetailView):

    """ HullDetail Definition """

    model = Hull


class HullSearchView(View):

    """ HullSearchView Definition """

    def get(self, request):
        form = SearchForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            country = form.cleaned_data.get("country")
            price = form.cleaned_data.get("price")

            filter_args = {}

            if name is not None:
                filter_args["name__startswith"] = name

            if country != "":
                filter_args["country"] = country

            if price is not None:
                filter_args["country"] = country

            qs = Hull.objects.filter(**filter_args).order_by("-created")
            paginator = Paginator(qs, 10, orphans=5)
            page = request.GET.get("page", 1)
            hulls = paginator.get_page(page)

            return render(request, "hulls/search.html", {"form": form, "hulls": hulls})

        return render(
            request,
            "hulls/search.html",
            {
                "form": form,
            },
        )
