from django.urls import re_path, path

from .views import DajaxiceRequest

urlpatterns = [
    re_path(r'^(.+)/$', DajaxiceRequest.as_view(), name='dajaxice-call-endpoint'),
    path('', DajaxiceRequest.as_view(), name='dajaxice-endpoint'),
]
