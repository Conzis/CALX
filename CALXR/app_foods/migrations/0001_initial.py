# Generated by Django 4.2.2 on 2023-06-25 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('cal', models.IntegerField()),
                ('is_premium', models.BooleanField(null=True)),
            ],
        ),
    ]
