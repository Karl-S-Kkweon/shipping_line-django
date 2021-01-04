from django.urls import path
from . import views


app_name = "owners_tmplt"


urlpatterns = [
    path("", views.OwnerList.as_view(), name="list"),
    path("<int:pk>", views.OwnerDetail.as_view(), name="detail"),
]
