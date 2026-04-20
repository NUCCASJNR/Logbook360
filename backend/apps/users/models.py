from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from apps.common.base_model import BaseModel
from .managers import UserManager


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        SUPERVISOR = "SUPERVISOR", "Supervisor"
        STUDENT = "STUDENT", "Student"

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # for admin panel

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    objects = UserManager()

    def __str__(self):
        return self.email