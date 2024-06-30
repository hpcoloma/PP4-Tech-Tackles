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

class Ticket(models.Model):
    STATUS_OPTIONS = (
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    )

    ticket_id = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    tech_support = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_tickets")
    subject = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_OPTIONS, default='Open')
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.ticket_id
