from rest_framework import viewsets, filters
from rest_framework.response import Response
from .models import Client, HealthProgram, Enrollment
from .serializers import ClientSerializer, HealthProgramSerializer, EnrollmentSerializer

# ViewSet for managing Clients
class ClientViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing clients.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name', 'contact_number']

# ViewSet for managing Health Programs
class HealthProgramViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing health programs.
    """
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer

# ViewSet for managing Enrollments
class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing enrollments.
    """
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

# Custom ViewSet for retrieving a client's profile
class ClientProfileViewSet(viewsets.ViewSet):
    """
    A ViewSet to retrieve the profile of a client.
    """

    def retrieve(self, request, pk=None):
        """
        Retrieve the profile of a client by their ID.
        """
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response({'detail': 'Client not found'}, status=404)

        serializer = ClientSerializer(client)
        return Response(serializer.data)
