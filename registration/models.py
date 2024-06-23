# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Airplanes(models.Model):
    airplaneid = models.AutoField(primary_key=True)
    airplanename = models.CharField(max_length=100)
    airplanecode = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'airplanes'


class Airports(models.Model):
    airportid = models.AutoField(primary_key=True)
    airportname = models.CharField(max_length=100)
    cityid = models.ForeignKey('Cities', models.DO_NOTHING, db_column='cityid', blank=True, null=True)
    airportcode = models.CharField(unique=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'airports'


class BookingStatus(models.Model):
    statusid = models.AutoField(primary_key=True)
    statusname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'booking_status'


class Bookings(models.Model):
    bookingid = models.AutoField(primary_key=True)
    flightid = models.ForeignKey('Flights', models.DO_NOTHING, db_column='flightid', blank=True, null=True)
    passengerid = models.ForeignKey('Passengers', models.DO_NOTHING, db_column='passengerid', blank=True, null=True)
    bookingdate = models.DateField()
    statusid = models.ForeignKey(BookingStatus, models.DO_NOTHING, db_column='statusid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookings'


class Cities(models.Model):
    cityid = models.AutoField(primary_key=True)
    cityname = models.CharField(max_length=100)
    citycode = models.CharField(unique=True, max_length=3)

    class Meta:
        managed = False
        db_table = 'cities'


class Flights(models.Model):
    flightid = models.AutoField(primary_key=True)
    routeid = models.ForeignKey('Routes', models.DO_NOTHING, db_column='routeid')
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'flights'


class Gender(models.Model):
    genderid = models.AutoField(primary_key=True)
    gendername = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'gender'

    def __str__(self):
        return self.gendername

class Passengers(models.Model):
    passengerid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dateofbirth = models.DateField()
    passportnumber = models.CharField(max_length=20)
    genderid = models.ForeignKey(Gender, models.DO_NOTHING, db_column='genderid', blank=True, null=True)
    flightid = models.ForeignKey(Flights, models.DO_NOTHING, db_column='flightid', blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passengers'


class Routes(models.Model):
    routeid = models.AutoField(primary_key=True)
    startairportid = models.ForeignKey(Airports, models.DO_NOTHING, db_column='startairportid')
    destinationairportid = models.ForeignKey(Airports, models.DO_NOTHING, db_column='destinationairportid', related_name='routes_destinationairportid_set')
    flightduration = models.IntegerField()
    airplaneid = models.ForeignKey(Airplanes, models.DO_NOTHING, db_column='airplaneid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'routes'


class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users'

# Create your models here.


def __str__(self):
    return self.title