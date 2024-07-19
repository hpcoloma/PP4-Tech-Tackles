from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField

# Create your models here.
# User profile model
ROLE_OPTIONS = (
    ('admin', 'Admin'),
    ('user', 'User'),
    ('tech_support', 'Tech Support'),  
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    surname = models.CharField(max_length=50, null=False, blank=False)
    role = models.CharField(max_length=20, choices=ROLE_OPTIONS, default='user')

def __str__(self):
    return f'{self.user.username} Profile'

class Ticket(models.Model):
    STATUS_OPTIONS = (
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    )

    ticket_id = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_OPTIONS, default='Open')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if it's a new ticket
            # Generate ticket_id logic as before
            date_str = datetime.now().strftime('%Y-%m%d')
            latest_ticket = Ticket.objects.filter(ticket_id__startswith=f'TT-{date_str}').order_by('created_on').last()
            if latest_ticket:
                last_ticket_number = int(latest_ticket.ticket_id[-3:])
                self.ticket_id = f'TT-{date_str}-{last_ticket_number + 1:03d}'
            else:
                self.ticket_id = f'TT-{date_str}-001'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.ticket_id


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter") # Many to one
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments', null=True, blank=True) # Many to one
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ticket_id} - {self.ticket} by {self.user}"