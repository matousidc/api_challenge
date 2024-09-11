from django.urls import path
from django.views.generic import RedirectView
from .views import CountryDetailView, CountryListView

urlpatterns = [
    path("", RedirectView.as_view(url="/countries", permanent=False)),
    path('countries/<int:pk>', CountryDetailView.as_view(), name='country-detail'),
    path('countries', CountryListView.as_view(), name='country-list'),
]
