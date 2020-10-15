from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")
    return_date = models.DateTimeField("Date of Return Visit", null=True)

    def __str__(self):
        return self.title


class ReportField(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    translation = models.TextField()