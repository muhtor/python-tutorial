from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_superuser=False):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), )
        user.set_password(password)
        user.is_superuser = is_superuser
        user.save()
        return user

    def create_staffuser(self, email, password):
        if not password:
            raise ValueError('staff/admins must have a password.')
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self, email, password):
        if not password:
            raise ValueError('superusers must have a password.')
        user = self.create_user(email, password=password, is_superuser=True)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        db_index=True,
        unique=True
    )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # email and password required by default

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

