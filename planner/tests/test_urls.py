import os
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from planner.views import home, about, itinerary, travel_plan

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'planMyTrip.settings'
class TestUrls(SimpleTestCase):
    
    def test_home_url_passed(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)
    
    def test_about_url_passed(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)
        
    def test_itinerary_url_passed(self):
        url = reverse('itinerary')
        self.assertEquals(resolve(url).func, itinerary)
        
    def test_travel_plan_url_passed(self):
        url = reverse('travel_plan')
        self.assertEquals(resolve(url).func, travel_plan)
