from django.db import models
from .bank import Bank


class Staff(models.Model):
    ROLES = [
        ("MANAGER", 'Manager'),
        ('CASHIER', 'Cashier'),
        ('SUPERVISOR', 'Supervisor'),
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    joined_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=ROLES)
    bank_id = models.ForeignKey(Bank, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
