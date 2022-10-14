from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user_registration'
