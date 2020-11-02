from django.urls import path
from . import views

app_name = "hulls"

urlpatterns = [path("list/", views.ListHullsView.as_view())]
