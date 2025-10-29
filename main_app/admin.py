from django.contrib import admin
# import your models here
from .models import Bookstore , Review

# Register your models here
admin.site.register(Bookstore)
admin.site.register(Review)