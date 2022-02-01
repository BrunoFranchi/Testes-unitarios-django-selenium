from django.contrib import admin

from animais.models import Animal

class Animais(admin.ModelAdmin):
    
    list_display = ('nome_animal','predador','venenoso','domestico')
    search_fields = ('nome_animal',)
    list_per_page = 20

admin.site.register(Animal, Animais)
