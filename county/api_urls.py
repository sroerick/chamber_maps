from rest_framework import routers

from county.api_views import CountyMapViewSet

router = routers.DefaultRouter()
router.register(r"counties", CountyMapViewSet)

urlpatterns = router.urls
