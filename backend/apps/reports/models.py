from apps.common.base_model import BaseModel, models
from apps.logbook.models import LogBook


class DailyLog(BaseModel):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    logbook = models.ForeignKey(
        LogBook,
        on_delete=models.CASCADE,
        related_name="daily_logs"
    )

    date = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    hours = models.PositiveIntegerField()

    week_number = models.PositiveIntegerField()
    month_number = models.PositiveIntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    supervisor_comment = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{self.date} - {self.title}"
