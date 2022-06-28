from tkinter import CASCADE
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Profession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    work = models.CharField(max_length=100, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.work
