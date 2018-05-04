from django.contrib import admin
from .models import Information 

class InformationAdmin(admin.ModelAdmin):
    list_display = ('SN','privateip','publicip','use','IDCid','locate','cpu','memory','datadisk')
    
admin.site.register(Information,InformationAdmin)

