from rest_framework import status
from django.test import TestCase
from core.models import Client, Program
from rest_framework.test import APIClient


class HealthSystemTests(TestCase):

    def setUp(self):
        
        self.client = APIClient()

        
        self.program = Program.objects.create(name="HIV Program")

        # Create a client and enroll them in the 'HIV Program'
        self.client_data = {
            'first_name': 'otieno',
            'last_name': 'dan',
            'email': 'otieno.dan@example.com',
            'phone_number': '1234567890',
            'enrolled_programs': [self.program.id],  # Ensuring the client is enrolled in the 'HIV Program'
        }
        self.client_instance = Client.objects.create(**self.client_data)

        # Auth setup if needed
        self.client.credentials(HTTP_AUTHORIZATION='Bearer <your_token_here>')

    def test_create_client(self):
        # Valid client data
        valid_data = {
            'first_name': 'Will',
            'last_name': 'Smith',
            'email': 'will.smith@example.com',
            'phone_number': '0987654321',
            'enrolled_programs': [self.program.id],  # Enrolling in HIV Program
        }

        # Create a new client
        response = self.client.post('/api/clients/', valid_data, format='json')

        # Ensure the response status code is 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Ensure the client is correctly created with the expected data
        client = Client.objects.get(id=response.data['id'])
        self.assertEqual(client.first_name, 'otieno')
        self.assertEqual(client.last_name, 'Smith')
        self.assertEqual(client.email, 'will.smith@example.com')
        self.assertEqual(client.phone_number, '0987654321')
        self.assertTrue(client.enrolled_programs.filter(name="HIV Program").exists())

    def test_client_profile_view(self):
        # Fetch the client profile view (assuming the URL path is correct)
        response = self.client.get(f'/api/clients/{self.client_instance.id}/')

        # Ensure the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertIn("HIV Program", [program['name'] for program in response.data['enrolled_programs']])

        self.assertEqual(response.data['first_name'], self.client_instance.first_name)
        self.assertEqual(response.data['last_name'], self.client_instance.last_name)
        self.assertEqual(response.data['email'], self.client_instance.email)

    def tearDown(self):
    
        self.client_instance.delete()
        self.program.delete()

