from django.contrib import admin

from .models import Mentor, Opinion

class MentorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')
    
admin.site.register(Mentor, MentorAdmin)
admin.site.register(Opinion)
