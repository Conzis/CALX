# Generated by Django 4.2.2 on 2023-06-25 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_foods', '0002_food_special_price_alter_food_is_premium'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
