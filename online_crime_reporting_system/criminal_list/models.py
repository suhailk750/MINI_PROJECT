from django.db import models

# Create your models here.
class CriminalList(models.Model):
    cl_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=50)
    photo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'criminal_list'
