from rest_framework.routers import DefaultRouter
from . import views

app_name = "yard_departments"
router = DefaultRouter()
router.register("", views.ListYardDepartmentsView)


urlpatterns = router.urls
