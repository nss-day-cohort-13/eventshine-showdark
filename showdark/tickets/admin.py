from django.contrib import admin

from .models import User, Event, UserEvent, Venue

admin.site.register(User)
admin.site.register(Event)
admin.site.register(UserEvent)
admin.site.register(Venue)
