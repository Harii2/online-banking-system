from django.db import models
from enum import Enum


class Bank(models.Model):
    BANK_NAMES_CHOICES = [
        ('SBI', 'SBI'),
        ('UNION_BANK_OF_INDIA', 'UNION_BANK_OF_INDIA'),
        ('ICIC', 'ICIC'),
    ]
    name = models.CharField(max_length=128, choices=BANK_NAMES_CHOICES)
    ifsc_code = models.CharField(max_length=128, null=False, blank=False)
    branch = models.CharField(max_length=128, null=False, blank=False)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
