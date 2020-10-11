from django.contrib import admin

# Register your models here.
from caching.models import UserDetails

admin.site.register(UserDetails)
