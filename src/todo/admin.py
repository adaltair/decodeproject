from django.contrib import admin
from .models import CustomUser, Task

# Register your models here.
admin.site.register(Task)
admin.site.register(CustomUser)