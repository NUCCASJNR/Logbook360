from apps.users.models import  BaseModel, models, School


class SIWESSession(BaseModel):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="sessions"
    )
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()


    def clean(self):
        from django.core.exceptions import ValidationError

        if self.end_date <= self.start_date:
            raise ValidationError("End date must be after start date")

    def __str__(self):
        return f"{self.name} ({self.school.name})"