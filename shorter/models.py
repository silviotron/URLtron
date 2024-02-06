import secrets
import string
from django.db import models
from django.contrib.auth.models import User

def generate_unique_key():
    """Generate a unique random string of 6 characters."""
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(6))
# Create your models here.
class Link(models.Model):
    # Default Django field for the primary key (id)
    # No need to declare it explicitly, as it's added automatically

    # URL to which the link redirects
    url = models.URLField()

    # Random character string (adjust the length as needed)
    key = models.CharField(max_length=6, unique=True, default=generate_unique_key, editable=False)

    # User ID who creates the link (foreign key to Django User table)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # Automatic creation date and time
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        user_username = self.user.username if self.user else 'None'
        return f"Link - ID: {self.id}, Key: {self.key}, Created at: {self.created_at}, User: {user_username}, URL: {self.url}"
