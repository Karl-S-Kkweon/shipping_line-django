from rest_framework.routers import DefaultRouter
from . import views

app_name = "manufacturers"
router = DefaultRouter()
router.register("", views.ListManufacturersView)

urlpatterns = router.urls
