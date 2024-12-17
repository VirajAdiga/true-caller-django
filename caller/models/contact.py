from django.db import models

from caller.models.user import User


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'phone_number')
        ordering = ['name']  # Order by name field by default

    def __str__(self):
        return self.name
