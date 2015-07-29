from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet

__author__ = 'smuravko'

router = DefaultRouter()
router.register(r'documents', DocumentViewSet, base_name='document-viewset')

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^task/', include('task.urls')),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

