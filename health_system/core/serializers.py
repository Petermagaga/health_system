from rest_framework import serializers
from health_system.core.models import Client, HealthProgram, Enrollment

class HealthProgramSerializer(serializers.ModelSerializer):
    # To include the related health programs, as it's a many-to-many field
    enrolled_programs = serializers.PrimaryKeyRelatedField(queryset=HealthProgram.objects.all(), many=True)

    class Meta:
        model = HealthProgram
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    # Simple serializer to represent the Client model
    class Meta:
        model = Client
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    # Serializer for Enrollment model
    class Meta:
        model = Enrollment
        fields = '__all__'


class ClientProfileSerializer(serializers.ModelSerializer):
    # This serializer will represent a specific Client's profile
    enrolled_programs = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'full_name', 'age', 'contact_number', 'enrolled_programs']

    def get_enrolled_programs(self, obj):
        # Here, we return the program names associated with this client
        return [en.program.name for en in obj.enrollments.all()]
