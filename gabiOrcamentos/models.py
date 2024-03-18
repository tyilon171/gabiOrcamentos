from django.db import models


# Create your models here.

class Location(models.Model):
    streetAddress = models.CharField(max_length=250)
    postalCode = models.CharField(max_length=10)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)

    def __str__(self):
        return self.streetAddress + ' - ' + self.postalCode + ' - ' + self.city + ' - ' + self.state


class Client(models.Model):
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    document = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phoneNumber = models.CharField(max_length=30)
    location = models.ForeignKey(Location, on_delete=models.RESTRICT)

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Schedule(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.client.email + ' - ' + self.date.isoformat()
