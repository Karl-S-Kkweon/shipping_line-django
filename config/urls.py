"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("core.urls")),
    path("hulls/", include("hulls.urls_tmplt", namespace="hulls_tmplt")),
    path("owners/", include("owners.urls_tmplt", namespace="owners_tmplt")),
    path("admin/", admin.site.urls),
    path("api/v1/hulls/", include("hulls.urls")),
    path("api/v1/owners/", include("owners.urls")),
    path("api/v1/hull_reports/", include("hull_report.urls")),
    path("api/v1/warranty_details/", include("Warranty_Details.urls")),
    path("api/v1/comm_logs/", include("communication_logs.urls")),
    path("api/v1/partners/", include("manufacturers.urls")),
    path("api/v1/departments/", include("yard_departments.urls")),
    path("api/v1/relevant_groups/", include("relevant_groups.urls")),
]
