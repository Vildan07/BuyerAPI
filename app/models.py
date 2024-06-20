from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Buyer(models.Model):
    """
    Model for Buyer
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
