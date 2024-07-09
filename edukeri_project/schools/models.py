from django.db import models

# Create your models here.

class Schools(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=100)
    number_of_teachers = models.IntegerField()

    def __str__(self):
     return f"{self.school_name}"