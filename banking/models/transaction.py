from django.db import models
from .account import Account


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('DEBIT', 'DEBIT'),
        ('CREDIT', 'CREDIT'),
    ]
    from_account_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="from_account_id")
    to_account_id = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="to_account_id")
    amount = models.IntegerField()
    type = models.CharField(max_length=6, choices=TRANSACTION_TYPE)
    made_at = models.DateTimeField(auto_now_add=True)
