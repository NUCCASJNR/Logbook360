from apps.common.base_model import BaseModel, models
from apps.logbook.models import LogBook
from apps.users.profile import SupervisorProfile

class WeeklyReview(BaseModel):
    logbook = models.ForeignKey(
        LogBook,
        on_delete=models.CASCADE,
        related_name="weekly_reviews"
    )
    week_number = models.PositiveIntegerField()
    comment = models.TextField()
    supervisor = models.ForeignKey(
        SupervisorProfile,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = "weekly_reviews"
        verbose_name = "Weekly Review"
        verbose_name_plural = "Weekly Reviews"


class MonthlyReview(BaseModel):
    logbook = models.ForeignKey(
        LogBook,
        on_delete=models.CASCADE,
        related_name="monthly_reviews"
    )
    month_number = models.PositiveIntegerField()
    student_summary = models.TextField()
    supervisor_comment = models.TextField(null=True, blank=True)
    supervisor = models.ForeignKey(
        SupervisorProfile,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = "monthly_reviews"
        verbose_name = "Monthly Review"
        verbose_name_plural = "Monthly Reviews"
