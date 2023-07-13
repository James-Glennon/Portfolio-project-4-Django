from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('bookings/', views.bookings_view, name='bookings'),
]
