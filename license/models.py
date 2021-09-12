from django.db import models

# Create your models here.
class generalReminder(models.Model):
    reminder_name=models.CharField(max_length=100)
    reminder_date=models.DateField()
    reminder_desc=models.CharField(max_length=300)
    reminder_time=models.TimeField()
    reminder_prenotice=models.IntegerField() 
    reminder_replay=models.CharField(max_length=30)

