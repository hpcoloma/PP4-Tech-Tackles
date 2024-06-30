from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Profile Model
class Profile(models.Model):
    ROLE_OPTIONS = (
        ('Admin', 'Admin'),
        ('User', 'User'),
        ('Tech Support', 'Tech Support'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_OPTIONS, default='User')

    def __str__(self):
        return self.user.username