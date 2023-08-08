from django.db import models

# Create your models here.
class BMR(models.Model):
    GENDER = [
        ('ชาย', 'ชาย'),
        ('หญิง','หญิง'),
    ]
    gender = models.CharField(max_length=10, choices= GENDER)
    weight = models.IntegerField(null=False)
    high = models.IntegerField(null=False)
    age = models.IntegerField()
    dateinfo = models.DateTimeField(auto_now_add=True)
