from django.db import models
from user_registration.models import UserRegistration


# Create your models here.
class Complaint(models.Model):
    c_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(UserRegistration,to_field='user_id',on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    phone = models.IntegerField()
    location = models.CharField(max_length=40)
    complaint = models.CharField(max_length=100)
    photo = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    reply = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'complaint'
