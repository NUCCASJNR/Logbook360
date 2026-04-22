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
