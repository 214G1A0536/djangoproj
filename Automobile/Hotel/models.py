from django.db import models
class Menu(models.Model):
    name=models.CharField(max_length=30)
    Price=models.IntegerField()
    type=models.CharField(max_length=30)
    def __str__(self):
        return self.name
# Create your models here.
