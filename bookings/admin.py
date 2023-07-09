from django.contrib import admin
from .models import Guest, Tables, Booking
# Register your models here.

admin.site.register(Guest)
admin.site.register(Tables)
admin.site.register(Booking)
