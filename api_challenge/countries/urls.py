from django.urls import path
from .views import CountryDetailView, CountryListView

urlpatterns = [
    path('countries/<int:pk>/', CountryDetailView.as_view(), name='country-detail'),
    path('countries/', CountryListView.as_view(), name='country-list'),
]
