from django.db import models

# Create your models here.

class Food(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    cal = models.IntegerField()
    is_premium = models.BooleanField(default=False)
    description = models.TextField(null=True)

def __str__(self):
    return self.title