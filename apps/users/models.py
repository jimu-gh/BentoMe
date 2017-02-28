from __future__ import unicode_literals

from django.db import models

import bcrypt

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    student = models.BooleanField(default=True)
    stripe_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def set_password(self, clear_password):
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(clear_passwordencode('utf-8'), salt)

    def check_password(self, clear_password):
        return bcrypt.hashpw(clear_passwordencode('utf-8'), self.password.encode('utf-8')) == self.password
