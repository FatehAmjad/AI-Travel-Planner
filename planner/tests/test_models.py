import os
from django.test import TestCase
from django.contrib.auth.models import User
from planner.models import Post, TravelPlan

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'planMyTrip.settings'
class TestPostModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='This is a test post', author=self.user)
    
    def test_post_str_representation(self):
        self.assertEqual(str(self.post), 'Test Post')
        
    def test_post_has_author(self):
        self.assertEqual(self.post.author, self.user)
        
class TestTravelPlanModel(TestCase):
    def setUp(self):
        self.travel_plan = TravelPlan.objects.create(
            firstname='Muhammed',
            lastname='Yaseen',
            destination='Sharjah',
            age=30,
            contact_number='9712244667',
            start_date='2022-01-01',
            end_date='2022-01-10',
            budget=1000,
            places='Majaz Waterfront, Ain Dubai',
            no_of_visitors=1,  # Provide a value for the no_of_visitors field
            booked_before=True,
            find='Google'
        )

    def test_travel_plan_str_representation(self):
        self.assertEqual(str(self.travel_plan), 'Muhammed Yaseen')

