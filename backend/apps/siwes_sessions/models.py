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
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "siwes_sessions"
        verbose_name = "SIWES Session"
        verbose_name_plural = "SIWES Sessions"

    def __str__(self):
        return f"{self.name} - {self.school.name}"
