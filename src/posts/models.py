from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        # how the model is displayed
        return self.title
