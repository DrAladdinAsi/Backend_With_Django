# Generated by Django 4.2.6 on 2023-10-23 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_airlines_airline_rename_hotels_hotel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]