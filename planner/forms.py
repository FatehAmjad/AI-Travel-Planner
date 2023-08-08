from django import forms
from .models import TravelPlan

class TravelPlanForm(forms.ModelForm):
    class Meta:
        model = TravelPlan
        fields = ['destination', 'start_date', 'end_date']
        # add any other fields for your form
