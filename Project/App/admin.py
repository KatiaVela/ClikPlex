from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Contact)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(Hall)
admin.site.register(Showing)
admin.site.register(Category)
admin.site.register(Reservation)