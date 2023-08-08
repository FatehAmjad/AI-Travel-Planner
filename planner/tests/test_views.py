import os
from django.test import TestCase, Client
from django.urls import reverse
from planner.models import TravelPlan

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'planMyTrip.settings'

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.about_url = reverse('about')
        self.travel_plan_url = reverse('travel_plan')
        self.itinerary_url = reverse('itinerary')
        
    def test_home_view(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planner/home.html')
        
    def test_about_view(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planner/about.html')
        
    def test_travel_plan_view(self):
        response = self.client.get(self.travel_plan_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planner/create_travel_plan.html')
        
    def test_itinerary_view(self):
        response = self.client.get(self.itinerary_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'planner/itinerary.html')
    
    # def test_travel_plan_post(self):
    #     # ... Add the test_travel_plan_post method code here 