from django.db import models

# Work Experience Model
class Blog(models.Model):
    position = models.CharField(max_length=50)
    companyname = models.CharField(max_length=50, blank=True)
    startdate = models.DateField(blank=True)
    enddate = models.DateField(blank=True, null = True)
    worklocation = models.CharField(max_length=50,blank=True)
    companydescription = models.TextField(null=True, blank=True)
    jobdescription = models.TextField(null=True,blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.position