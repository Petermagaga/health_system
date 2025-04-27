from rest_framework import viewsets, filters
from rest_framework.response import Response
from .models import Client, HealthProgram, Enrollment
from .serializers import ClientSerializer, HealthProgramSerializer, EnrollmentSerializer


class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'contact_number']


class HealthProgramViewSet(viewsets.ModelViewSet):

    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer
s
class EnrollmentViewSet(viewsets.ModelViewSet):
 
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class ClientProfileViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
       
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response({'detail': 'Client not found'}, status=404)

        serializer = ClientSerializer(client)
        return Response(serializer.data)
