#!usr/bin/env python3

""" Contain Student and supervisor Profile models. """

from apps.common.base_model import BaseModel, models


class StudentProfile(BaseModel):
    user = models.OneToOneField(
        "User",
        on_delete=models.CASCADE,
        related_name="student_profile"
    )
    matric_number = models.CharField(max_length=50, unique=True)
    department = models.ForeignKey(
        "Department",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # Assigned supervisor
    supervisor = models.ForeignKey(
        "SupervisorProfile",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students"
    )

    # Current SIWES session
    session = models.ForeignKey(
        "siwes_sessions.SIWESSession",
        on_delete=models.CASCADE,
        related_name="students"
    )

    def __str__(self):
        return f"{self.user.email} ({self.matric_number})"


class SupervisorProfile(models.Model):
    user = models.OneToOneField(
        "User",
        on_delete=models.CASCADE,
        related_name="supervisor_profile"
    )

    department = models.ForeignKey(
        "Department",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    max_students = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}"


class Department(BaseModel):
    school = models.ForeignKey(
        "School",
        on_delete=models.CASCADE,
        related_name="departments"
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name