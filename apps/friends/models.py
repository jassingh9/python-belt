# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
from datetime import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.


class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Name is required and must be greater than 2 characters."
        if postData['name'].isalpha() == False:
            errors['name'] = "Name must be letters only."
        if len(postData['alias']) < 2:
            errors['alias'] = "Alias is required and must be greater than 2 characters."
        if postData['alias'].isalpha() == False:
            errors['alias'] = "Alias must be letters only."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be a valid format."
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors['email'] = "Email in use"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be greater than 8 characters."
        if postData['password'] != postData['conf_password']:
            errors['password_match'] = "Passwords must match."
        try:
            if postData['birthday'] != datetime.strptime(postData['birthday'], "%Y-%m-%d").strftime('%Y-%m-%d'):
                errors['birthday'] = "Enter a birthday."
        except ValueError:
            errors['birthday'] = "Enter a birthday."

        return errors

    def login_validator(self, postData):
        errors = {}


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField()
    objects = UserManager()


class Friend(models.Model):
    client_friend = models.ForeignKey(User, related_name="friend_sender")
    receive_friend = models.ForeignKey(User, related_name="friend_receiver")
