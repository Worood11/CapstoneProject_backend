from django.contrib import admin
# import your models here
from .models import Bookstore , Review , Event

# Register your models here
admin.site.register(Bookstore)
admin.site.register(Review)
admin.site.register(Event)