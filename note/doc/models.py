from django.db import models

# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=800)

    def _str_(self):
        return self.title

