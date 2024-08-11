from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class POST(models.Model):
    users=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="media")
    caption=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.caption
