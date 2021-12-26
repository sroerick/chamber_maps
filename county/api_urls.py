from rest_framework import routers

from county.api_views import CountyMapViewSet, ExampleDataViewSet, ExampleDataNokeyViewSet


router = routers.DefaultRouter()
router.register(r"counties", CountyMapViewSet)
router.register(r"example", ExampleDataViewSet)
router.register(r"example2", ExampleDataNokeyViewSet)
#router.register(r"map", UploadedDataViewSet)

urlpatterns = router.urls
