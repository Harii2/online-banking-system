# Generated by Django 3.0.5 on 2023-09-12 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0005_auto_20230911_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='made_at',
            new_name='date_time',
        ),
    ]