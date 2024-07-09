from django.db import models
from schools.models import Schools

# Create your models here.
class Administrators(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=50)
    admin_school = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name='administrators')
    admin_email = models.EmailField(max_length=254)
    admin_password = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.admin_name}"
    








