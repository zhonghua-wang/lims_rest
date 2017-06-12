from django.conf.urls import url, include
from rest_framework import routers
from instrument import views


router = routers.DefaultRouter()
router.register(r'department', views.DepartmentViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]