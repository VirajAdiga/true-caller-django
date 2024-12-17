from django.db import models

from caller.models.user import User


class SpamReport(models.Model):
    phone_number = models.CharField(max_length=15)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()

    class Meta:
        ordering = ['phone_number']  # Order by phone_number field by default

    def __str__(self):
        return f"{self.phone_number} reported by {self.reported_by.phone_number}"
