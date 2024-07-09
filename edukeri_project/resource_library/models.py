from django.db import models

# Create your models here.

class Resource_Library(models.Model):
    resource_id = models.AutoField(primary_key=True)
    resource_title = models.CharField(max_length=200)
    resource_video = models.FileField()
    resource_url = models.TextField()

    def __str__(self):
        return f"{self.resource_title}"
