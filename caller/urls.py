from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, ContactListView, ContactDetailView, SpamReportView, SearchView, SearchByPhoneNumberView, LogoutView, DetailedView

urlpatterns = [

    # Users
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Contacts
    path('contacts/', ContactListView.as_view(), name='contact-list'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),

    # Spam reporting
    path('report-spam/', SpamReportView.as_view(), name='report-spam'),

    # Search
    path('search/', SearchView.as_view(), name='search'),
    path('search-by-phone/', SearchByPhoneNumberView.as_view(), name='search-by-phone'),
    path('details/<str:phone_number>/', DetailedView.as_view(), name='detailed-view'),
]
