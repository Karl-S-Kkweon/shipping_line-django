from rest_framework.routers import DefaultRouter
from . import views

app_name = "owners"
router = DefaultRouter()
router.register("", views.OwnersViewSet)


urlpatterns = router.urls
