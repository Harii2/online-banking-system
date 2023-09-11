# your django admin
from banking.models import Bank, Staff
from django.contrib import admin

admin.register(Bank)
admin.register(Staff)