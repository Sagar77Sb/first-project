from django.contrib import admin
from .models import *

admin.site.register(Registration)

class RegistrationAdmin(admin.ModelAdmin):
    list_display=['useranme','name','email','mobile_no','password']
