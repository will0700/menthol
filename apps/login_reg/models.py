from django.db import models
from django.core.validators import validate_email

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1 or not postData['first_name'].isalpha():
            errors['first_name'] = "First name must be at least 2 characters and only alphabets"
        if len(postData['last_name']) < 1 or not postData['last_name'].isalpha():
            errors['last_name'] = "Last name must be at least 2 characters and only alphabets"
        try:
            validate_email(postData['email'])
        except:
            errors['email'] = "Email invalid format"
        if len(postData['password']) < 7:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['password_c']:
            errors['password_c'] = "Password Confirmation invalid"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=90)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()