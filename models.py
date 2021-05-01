from django.db import models

# Create your models here.

class DriverDetails(models.Model):
    driver_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'driver'

class RideDetals(models.Model):
    create_date = models.DateTimeField()
    start_loc = models.CharField(max_length=50)
    end_loc = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    customer_id = models.IntegerField()
    driver_id = models.IntegerField()

    class Meta:
        managed =False
        db_table = 'ride_details'
