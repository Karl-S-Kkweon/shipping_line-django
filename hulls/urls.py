from rest_framework.routers import DefaultRouter
from . import views

app_name = "hulls"
router = DefaultRouter()
router.register("", views.ListHullsView)


urlpatterns = router.urls
