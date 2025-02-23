from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password

class HRManager(models.Model):
    id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=50)
    ManagerID = models.CharField(
        max_length=4,
        validators=[RegexValidator(r'^\d{4}$', 'Manager ID must be exactly 4 digits')],
        unique=True,
        default='0000'
    )
    password = models.CharField(max_length=128)  # Increased max_length to accommodate hashed passwords

    def save(self, *args, **kwargs):
        # If password is not already hashed, hash it before saving
        if not self.password.startswith('pbkdf2_sha256$'):  # Checking if the password is already hashed
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
