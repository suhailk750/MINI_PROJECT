from django.db import models

# Create your models here.
class EmergencyNumber(models.Model):
    e_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'emergency_number'
