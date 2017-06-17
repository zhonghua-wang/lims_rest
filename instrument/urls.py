from django.conf.urls import url, include
from rest_framework import routers
from instrument import views

router = routers.DefaultRouter()
router.register(r'department', views.DepartmentViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'instrument', views.InstrumentViewSet)
router.register(r'reservation', views.ReservationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),

]
