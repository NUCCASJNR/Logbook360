#!/usr/bin/env python3

"""
Contains Logbook Model and other related funcs
"""
from apps.users.models import BaseModel, models, School
from apps.users.profile import StudentProfile, SupervisorProfile
from apps.siwes_sessions.models import SIWESSession


class LogBook(BaseModel):
    """
    LogBook Model
    """
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="logbooks"
    )
    session = models.ForeignKey(
        SIWESSession,
        on_delete=models.CASCADE,
        related_name="logbooks"
    )

    student = models.OneToOneField(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name="logbook"
    )

    supervisor = models.ForeignKey(
        SupervisorProfile,
        on_delete=models.SET_NULL,
        null=True,
        related_name="logbooks"
    )

    class Meta:
        db_table = "logbooks"
        verbose_name = "Logbook"
        verbose_name_plural = "Logbooks"


    def __str__(self):
        return f"LogBook - {self.student.user.email}"
