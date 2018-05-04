from django.contrib import admin
from .models import monitors,Experience

class monitorAdmin(admin.ModelAdmin):
    list_display = ('servername','item','value','serverip','time')

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title','author','timestamp')
    
admin.site.register(monitors,monitorAdmin)
admin.site.register(Experience,ExperienceAdmin)


