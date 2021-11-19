from django.conf.urls import url
from . import views


app_name = 'county'

urlpatterns = [
    # city detail view
    url(r'^county/(?P<pk>[0-9]+)$',
        views.CountyDetailView.as_view(), name='county-detail'),
]
