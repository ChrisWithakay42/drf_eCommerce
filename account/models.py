from typing import Self

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email: str, username: str, password: str, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned as a staff member'
            )
        if kwargs.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have the value Superuser set to True'
            )

        return self.create_user(email, username, password, **kwargs)

    def create_user(self, email: str, username: str, password: str, **kwargs):

        if not email:
            raise ValueError(
                'Email address is missing!'
            )
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user


class UserBase(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150, unique=True)

