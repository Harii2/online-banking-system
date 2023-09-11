from django.db import models
from .bank import Bank


class Staff(models.Model):
    ROLES = [
        ("MANAGER", 'Manager'),
        ('CASHIER', 'Cashier'),
        ('SUPERVISOR', 'Supervisor'),
    ]
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobile_number = models.CharField(max_length=255, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=255, choices=ROLES)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
