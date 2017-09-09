from django.conf.urls import url
from .views import *

app_name = 'hr'

urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^position/add/$', PositionAdd.as_view(), name='position_add'),
    url(r'^position/(?P<position_id>[0-9]+)/delete/$', PositionDelete.as_view(), name='position_delete'),
    url(r'^position/(?P<position_id>[0-9]+)/edit/$', PositionEdit.as_view(), name='position_edit'),
    url(r'^position/list/$', PositionList.as_view(), name='position_list'),
    url(r'^position/(?P<position_id>[0-9]+)/detail/$', PositionDetail.as_view(), name='position_detail'),

    url(r'^staff/add/$', StaffAdd.as_view(), name='staff_add'),
    url(r'^staff/(?P<staff_id>[0-9]+)/delete/$', StaffDelete.as_view(), name='staff_delete'),
    url(r'^staff/(?P<staff_id>[0-9]+)/edit/$', StaffEdit.as_view(), name='staff_edit'),
    url(r'^staff/list/$', StaffList.as_view(), name='staff_list'),
    url(r'^staff/(?P<staff_id>[0-9]+)/detail/$', StaffDetail.as_view(), name='staff_detail'),
]
