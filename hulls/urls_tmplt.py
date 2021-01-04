from django.urls import path
from . import views

app_name = "hulls_tmplt"


urlpatterns = [
    path("", views.HullList.as_view(), name="list"),
    path("search/", views.HullSearchView.as_view(), name="search"),
    path("<int:pk>", views.HullDetail.as_view(), name="detail"),
]
