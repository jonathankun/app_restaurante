from django.contrib import admin
from .models import Plato
from .models import Mesero
from .models import Cliente

# Register your models here.
#admin.site.register(Plato)

@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ('nombre','procedencia','precio')
    #list_filter = ('nombre','tipo')
    search_fields = ('nombre',)
    #fields = ('nombre',)

@admin.register(Mesero)
class MeseroAdmin(admin.ModelAdmin):
    list_display = ('nombre','procedencia','edad')
    #list_filter = ('nombre','tipo')
    #fields = ('nombre',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','dni')
    #list_filter = ('nombre','tipo')
    #fields = ('nombre',)