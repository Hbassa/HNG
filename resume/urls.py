from django.urls import path
from .views import CvView, Contact, Success, About

urlpatterns = [
    path('', CvView.as_view(), name='home'),
    path('contact', Contact.as_view(), name='contact_me'),
    path('success', Success.as_view(), name='success'),
    path('about', About.as_view(), name='about'),
]