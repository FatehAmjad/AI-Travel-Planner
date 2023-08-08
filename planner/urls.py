from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import SavePDFView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('itinerary/', views.itinerary, name='itinerary'),  # Add a trailing slash
    path('travel-plan/', views.travel_plan, name='travel_plan'),
    path('save_pdf_view/', SavePDFView.as_view(), name='save_pdf_view'),
] 
