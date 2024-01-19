from django.db import models

class register(models.Model):
    email = models.EmailField(max_length=50, unique=True)  # Add unique constraint
    Mobile_number = models.CharField(max_length=10, unique=True)  # Add unique constraint
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email

