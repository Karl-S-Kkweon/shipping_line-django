from rest_framework.routers import DefaultRouter
from . import views

app_name = "communication_logs"
router = DefaultRouter()
router.register("", views.ListCommunicationLogsView)


urlpatterns = router.urls
