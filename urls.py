from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index, name='all-meetups'), #out-domain.com/meetups
    path('meetup/<slug:meetup_slug>', views.meetup_details, name='meetup-detail'),
]