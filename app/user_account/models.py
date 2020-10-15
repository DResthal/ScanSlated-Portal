from django.db import models
from django.conf import settings

class Report(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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

class ReportFindings(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    description = models.TextField()
    translation = models.TextField()