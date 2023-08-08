import os
from django.test import TestCase
from django.contrib.auth.models import User
from planner.forms import TravelPlanForm

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'planMyTrip.settings'

class TravelPlanFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_valid_form_data(self):
        form = TravelPlanForm(data={
            'firstname': 'John',
            'lastname': 'Doe',
            'destination': 'New York',
            'age': 30,
            'contact_number': '1234567890',
            'start_date': '2023-07-01',
            'end_date': '2023-07-10',
            'budget': 1000,
            'places': ['Place 1', 'Place 2'],
            'no_of_adults': 2,
            'no_of_children': 1,
            'no_of_events': 3,
            'booked_before': True,
            'find': 'Online'
        })
        self.assertTrue(form.is_valid())

# Uncomment the method below to test_invalid_form_data.

    # def test_invalid_form_data(self):
    #     form = TravelPlanForm(data={
    #         'firstname': '',
    #         'lastname': 'Doe',
    #         'destination': 'New York',
    #         'age': 30,
    #         'contact_number': '1234567890',
    #         'start_date': '2023-07-01',
    #         'end_date': '2023-07-10',
    #         'budget': 1000,
    #         'places': ['Place 1', 'Place 2'],
    #         'no_of_adults': 2,
    #         'no_of_children': 1,
    #         'no_of_events': 3,
    #         'booked_before': True,
    #         'find': 'Online'
    #     })

    #     # Check that the form is not valid
    #     self.assertFalse(form.is_valid())

    #     # Check that the 'firstname' field has a validation error
    #     self.assertEqual(len(form.errors), 1)
    #     self.assertTrue('firstname' in form.errors)

