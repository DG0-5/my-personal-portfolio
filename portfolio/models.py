from django.db import models

# Education Model
class Education(models.Model):
    degree = models.CharField(max_length=75)
    university = models.CharField(max_length=75, blank=True)
    startdate = models.DateField(blank=True)
    enddate = models.DateField(blank=True, null = True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=50, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.degree
