"""chamber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings

from django.conf.urls.static import static
from county.views import CountyDataView, ExampleDataView, ExampleDataNokeyView, UploadedDataView
from county.admin import mapAdmin, admin_csv_import
from county.api_views import UploadedDataAPIView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('import/', admin_csv_import.urls, name='import'),
    #path('admin/map', mapAdmin.asview()),
    path("map/", CountyDataView.as_view()),
    path("map/<slug:slug>/", UploadedDataView.as_view()),
    path("api/map/<slug:slug>/", UploadedDataAPIView.as_view()),
    path("example/", ExampleDataView.as_view()),
    path("example2/", ExampleDataNokeyView.as_view()),
    path("api/", include('county.api_urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
