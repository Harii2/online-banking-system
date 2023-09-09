from django.db import models
from .bank import Bank


class Account(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.TextField()
    mobile_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    balance = models.IntegerField(default=0)
    bank_id = models.ForeignKey(Bank, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
