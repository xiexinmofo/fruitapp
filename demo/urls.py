from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^json_response/$',views.json_response,name='json_response'),
    url(r'^(\d+)/$',views.good_detail,name='good_detail'),
]