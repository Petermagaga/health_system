from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet,EnrollmentViewSet,HealthProgramViewSet,ClientProfileViewSet


router=DefaultRouter()
router.register('clients',ClientViewSet)
router.register('programs',HealthProgramViewSet)
router.register('enrollments',EnrollmentViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('clients/<int:pk>/profile/', ClientProfileViewSet.as_view({'get': 'retrieve'}), name='client-profile'),
]