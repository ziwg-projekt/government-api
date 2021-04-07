from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    pesel = models.CharField(max_length=11)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=9, null=True, blank=True)

    def __str__(self):
        return f"{self.pesel} - {self.name} {self.surname}"
