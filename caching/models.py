from django.db import models

# Create your models here.


class UserDetails(models.Model):
    name = models.CharField(max_length=125)
    address = models.TextField(null=True, blank=True)
    age = models.IntegerField(default=18)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
