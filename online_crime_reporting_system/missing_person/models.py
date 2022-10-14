from django.db import models

# Create your models here.
class MissingPerson(models.Model):
    ml_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'missing_person'

