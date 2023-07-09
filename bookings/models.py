from django.db import models

# Create your models here.


class Guest(models.Model):
    """ Model for user login/ registration """
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    company_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=False, null=False)
    password = models.CharField(blank=False, null=False, max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tables(models.Model):
    """ Model for the restaurant Dining Tables """
    table_id = models.PositiveIntegerField(primary_key=True, default=1)
    date = models.DateField(blank=False, null=False)
    time = models.TimeField(blank=False, null=False)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.table_id} {self.date} {self.time}'


class Booking(models.Model):
    """ Model for Individual bookings """
    user_id = models.ForeignKey(Guest, on_delete=models.CASCADE)
    booking_name = models.CharField(max_length=100,
                                    default=f'{Guest.first_name} {Guest.last_name}', blank=False)
    table_id = models.ForeignKey(Tables, on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False)
    time = models.TimeField(blank=False, null=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.booking_name},{Tables.date},{Tables.time}'
