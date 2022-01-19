from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from django.conf.urls.static import static
from county.views import CountyDataView, ExampleDataView, ExampleDataNokeyView, UploadedDataView, IndexView, OLMapView
from county.admin import mapAdmin, admin_csv_import
from county.api_views import UploadedDataAPIView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('import/', admin_csv_import.urls, name='importcsv'),
    path("map/", CountyDataView.as_view()),
    path("map/<slug:slug>/", UploadedDataView.as_view(), name="map"),
    path("olmap/<slug:slug>/", OLMapView.as_view(), name="map"),
    path("api/map/<slug:slug>/", UploadedDataAPIView.as_view()),
    path("example/", ExampleDataView.as_view()),
    path("example2/", ExampleDataNokeyView.as_view()),
    path("api/", include('county.api_urls')),
    path("county/", include('county.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
