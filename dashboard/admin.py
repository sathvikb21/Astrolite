from django.contrib import admin
from .models import Event, Ticket, Order

admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(Order)
