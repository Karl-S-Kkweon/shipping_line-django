from rest_framework.routers import DefaultRouter
from . import views

app_name = "relevant_groups"
router = DefaultRouter()
router.register("", views.ListRelevantGroupsView)


urlpatterns = router.urls
