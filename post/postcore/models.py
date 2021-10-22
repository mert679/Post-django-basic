
from django.conf import settings
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(blank=True)

#upload_to='media',
    class Meta:
        db_table = "post"
    def __str__(self):
        return self.title
