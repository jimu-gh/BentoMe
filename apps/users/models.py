from __future__ import unicode_literals

from django.db import models

import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def login(self, post_data):
        errors = []
        user = None
        try:
            user = User.objects.get(email=post_data['email'])
        except:
            errors.append("Incorrect Email/Password")
            return errors

        if user.check_password(post_data['password']):
            return user
        else:
            errors.append("Incorrect Email/Password")
            return errors

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    student = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    last_4_digits = models.CharField(max_length=4, default="0000")
    stripe_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return "{ Name: " + self.first_name + " " + self.last_name + " }"

    def set_password(self, clear_password):
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(clear_password.encode('utf-8'), salt)

    def check_password(self, clear_password):
        return bcrypt.hashpw(clear_password.encode('utf-8'), self.password.encode('utf-8')) == self.password

    def make_admin(self):
        self.admin = True
        user.save()

# class Message(models.Model):
#     user = models.ForeignKey(User, related_name="messages")
#     message = models.TextField(max_length=500)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
