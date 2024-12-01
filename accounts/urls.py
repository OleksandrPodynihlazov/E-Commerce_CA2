from django.urls import path
from .views import SignUpView,edit_profile,profile_view

app_name = 'accounts'

urlpatterns = [
    path('create/', SignUpView.as_view(), name='signup'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('profile/', profile_view, name='profile'),
]


