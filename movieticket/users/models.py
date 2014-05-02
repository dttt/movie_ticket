# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from facility.models import City


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_super_user(self, email, password=None):
        user = self.create_user(email, password=password,)
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.CharField(
        verbose_name="",
        max_length=255,
        unique=True,
    )

    name = models.CharField("", max_length=100)
    address = models.CharField("", max_length=255)
    card_id = models.CharField("", max_length=20)
    tel = models.CharField("", max_length=20)
    city = models.ForeignKey(City, verbose_name="")
    date_of_birth = models.DateField("")

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = ""
        verbose_name_plural = ""
