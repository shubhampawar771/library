from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta


class Book(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    class Meta:
        db_table='add books'

    def __str__(self):
        return str(self.name)

    @classmethod
    def create(cls, name, author, category):
        pass



def expiry():
    return datetime.today() + timedelta(days=14)
