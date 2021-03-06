# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin, AbstractBaseUser, BaseUserManager)
from django.utils import timezone


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('')

        user = self.model(
            email=self.normalize_email(email),
            name="",
            address="",
            card_id="",
            tel="",
            date_of_birth=timezone.now().date(),
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
    )

    name = models.CharField("Tên", max_length=100)
    address = models.CharField("Địa chỉ", max_length=255, blank=True)
    card_id = models.CharField("CMND", max_length=20)
    tel = models.CharField("Số điện thoại", max_length=20)
    date_of_birth = models.DateField("Ngày sinh", null=True)
    date_joined = models.DateTimeField("Ngày lập", default=timezone.now())

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []
    objects = CustomUserManager()

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
