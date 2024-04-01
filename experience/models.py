from django.db import models

# Project Description Model
class Experience(models.Model):
    title = models.CharField(max_length=50)
    backend = models.CharField(max_length=50, blank=True)
    frontend = models.CharField(max_length=50,blank=True)
    description = models.TextField(null=True, blank=True)
    code = models.URLField(blank=True)
    demo = models.URLField(blank=True)

    def __str__(self):
        return self.title
