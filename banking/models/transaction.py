from django.db import models
from .account import Account


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('DEBIT', 'DEBIT'),
        ('CREDIT', 'CREDIT'),
    ]
    from_account_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="from_account_id", null=True)
    to_account_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="account_id", null=True)
    amount = models.IntegerField()
    type = models.CharField(max_length=255, choices=TRANSACTION_TYPE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.from_account_id} {self.to_account_id} {self.amount} {self.type} {self.date_time}'
