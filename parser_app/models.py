from django.db import models

class CharterRecordWestshore(models.Model):
    date = models.CharField(max_length=100)
    vessel = models.CharField(max_length=255)
    charterer = models.CharField(max_length=255)
    scope_of_work = models.TextField()
    comm = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - {self.vessel}"


class CharterRecordBraemaroffshore(models.Model):
    date = models.CharField(max_length=100)
    vessel = models.CharField(max_length=255)
    charterer = models.CharField(max_length=255)
    scope_of_work = models.TextField()
    asset = models.CharField(max_length=255)
    period = models.CharField(max_length=255)
    onhire = models.CharField(max_length=255)
    rate = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - {self.vessel}"

class CharterRecordHowerobinsonoffshore(models.Model):
    date = models.CharField(max_length=100)
    vessel = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    charterer = models.CharField(max_length=255)
    scope_of_work = models.TextField()
    period = models.CharField(max_length=255)
    commencement = models.CharField(max_length=255)
    rate = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - {self.vessel}"