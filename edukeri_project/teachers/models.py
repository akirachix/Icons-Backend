from django.db import models

from courses.models import Courses
from schools.models import Schools

# Create your models here.

class Teachers(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField()
    bio = models.TextField(blank=True, null=True)
    teacher_school = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name='teachers')
    level_of_education = models.CharField(max_length = 10)
    subject = models.CharField(max_length=50)
    current_course_level = models.ForeignKey(Courses, on_delete=models.SET_NULL, null=True, related_name='courses')
    current_course_progress = models.IntegerField()
    achievement = models.TextField()
    feedback = models.TextField()

    def __str__(self):
     return f"{self.full_name}"
    
   
