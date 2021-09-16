# from django.contrib import admin
# from . models import Movie

# # Register your models here.

# admin.site.register(Movie)

from django.contrib import admin
from . models import Movie,contact,order
# Register your models here.
admin.site.register(Movie)
admin.site.register(contact)
admin.site.register(order)

