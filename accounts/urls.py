from django.urls import path
from .api import CreateSponsorView, CreateCompanyView

urlpatterns = [
    path('reg/sponsor/',CreateSponsorView.as_view()),
    path('reg/company/', CreateCompanyView.as_view()),
]