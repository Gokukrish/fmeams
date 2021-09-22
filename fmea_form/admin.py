from django.contrib import admin
from .models import FmeaRegister, FmeaProcess

# Register your models here.

admin.site.register(FmeaRegister)
admin.site.register(FmeaProcess)
