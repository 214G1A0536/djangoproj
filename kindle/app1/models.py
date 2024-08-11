from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    rating=models.IntegerField()
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title=models.CharField(max_length=30,null=False, blank=False)
    price=models.IntegerField()
    gener=models.CharField(max_length=30)
    author=models.ForeignKey('Author',on_delete=models.CASCADE)
    def __str__(self):
        return self.title
# Create your models here.
