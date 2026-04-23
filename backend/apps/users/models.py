from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.common.base_model import BaseModel
from .managers import UserManager


class School(BaseModel):
    """
    School Model
    """
    name = models.TextField()
    address = models.TextField()

    class Meta:
        db_table = "schools"
        verbose_name = "School"
        verbose_name_plural = "Schools"


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        SUPERVISOR = "SUPERVISOR", "Supervisor"
        STUDENT = "STUDENT", "Student"

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )
    verified = models.BooleanField(default=False)
    verification_code = models.CharField(
        max_length=6,
        blank=True,
        null=True,
    )
    reset_token = models.CharField(
        max_length=6,
        blank=True,
        null=True,
    )
    school = models.OneToOneField(
        "School",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="user",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    objects = UserManager()

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.full_name}"
