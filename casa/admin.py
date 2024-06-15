from django.contrib import admin

# Register your models here.
from .models.casaModel import Casa


@admin.register(Casa)
class CasaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'foto',)