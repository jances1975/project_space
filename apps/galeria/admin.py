from django.contrib import admin
from apps.galeria.models import Fotografia

# Register your models here.


class listandofotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "foto", "categoria", "publicada", "usuario")
    list_display_links = ("id", "nome", "foto", "categoria")
    search_fields = ("nome",)
    list_filter = ("categoria", "publicada", "usuario")
    list_editable = ("publicada",)
    list_per_page = 10


# paginação 5 registros por tela do admin
# "nome", tem que ser uma tupla, ou seja, mais de campo pois isso a vírgula
admin.site.register(Fotografia, listandofotografias)
