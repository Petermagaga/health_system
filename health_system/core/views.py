from rest_framework import viewsets,generics,filters
from health_system.core.models import Client,HealthProgram,Enrollment
from .serializers import ClientSerializer,HealthProgramSerializer,EnrollmentSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset= Client.objects.all()
    serializer_class=ClientSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['full_name','contact_number']

class HealthProgramViewSet(viewsets.ModelViewSet):
    queryset=HealthProgram.objects.all()
    serializer_class=HealthProgramSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset=Enrollment.objects.all()
    serializer_class=EnrollmentSerializer

class ClientProfileViewSet(viewsets.ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer

