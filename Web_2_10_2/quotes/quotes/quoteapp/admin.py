from django.contrib import admin
from .models import Authors, Quotes

# Register your models here.
admin.site.register(Authors)
admin.site.register(Quotes)