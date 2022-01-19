from django.conf.urls import url
from . import views


app_name = 'county'

urlpatterns = [
    # city detail view
    url(r'^county/(?P<pk>[0-9]+)$',
        views.CountyDetailView.as_view(), name='county-detail'),
    #url(r'^signup$', views.signup, name='signup'),
    #url(r'^login', views.pagelogin, name='login'),
    url(r'^logout', views.logout_view, name='logout'),
]
