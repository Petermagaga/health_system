from rest_framework import serializers
from health_system.core.models import Client, HealthProgram, Enrollment

class HealthProgramSerializer(serializers.ModelSerializer):
    enrolled_programs = serializers.PrimaryKeyRelatedField(queryset=HealthProgram.objects.all(), many=True)

    class Meta:
        model = HealthProgram
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'


class ClientProfileSerializer(serializers.ModelSerializer):
    enrolled_programs = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'full_name', 'age', 'contact_number', 'enrolled_programs']

    def get_enrolled_programs(self, obj):
        return [en.program.name for en in obj.enrollments.all()]
