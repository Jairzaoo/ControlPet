from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    VACCINE_CHOICES = [
        ('V8', 'V8'),
        ('V10', 'V10'),
        ('Não Vacinado', 'Não Vacinado'),
    ]

    name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    consultation_date = models.DateField(null=True, blank=True)
    consultation_time = models.TimeField(null=True, blank=True)  # Add this field
    last_vaccine_date = models.DateField(null=True, blank=True)
    vaccine = models.CharField(max_length=15, choices=VACCINE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name