from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import CaseViewSet


router = DefaultRouter()
router.register(r'cases', CaseViewSet, base_name='cases')
urlpatterns = router.urls
