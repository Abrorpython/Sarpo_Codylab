from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    CHOICES = [

        ("Rahbar", "Rahbar"),
        ("Menejer", "Menejer"),
        ("Agent", "Agent")

    ]

    role = models.CharField(choices=CHOICES, max_length=20)