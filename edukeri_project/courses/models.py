from django.db import models

# Create your models here.

class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_level_title = models.CharField(max_length=100)
    course_description = models.TextField()
    course_picture= models.ImageField()
    course_progress = models.IntegerField()
    course_content = models.TextField()
    course_certificate = models.BooleanField()

    def __str__(self):
        return f"{self.course_level_title}"
    

