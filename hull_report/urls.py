from rest_framework.routers import DefaultRouter
from . import views

app_name = "hull_report"
router = DefaultRouter()
router.register("", views.ListHullReportView)


urlpatterns = router.urls
