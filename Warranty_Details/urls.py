from rest_framework.routers import DefaultRouter
from . import views

app_name = "Warranty_Details"
router = DefaultRouter()
router.register("", views.ListWarrantyDetailsView)

urlpatterns = router.urls
