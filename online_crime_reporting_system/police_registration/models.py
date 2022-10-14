from django.db import models

# Create your models here.
class PoliceRegistration(models.Model):
    pr_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'police_registration'
