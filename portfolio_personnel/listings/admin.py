from django.contrib import admin

from listings.models import Groupe

from listings.models import Article

class GroupeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'annee_formation', 'genre')#liste des champs qu'on veut ajouter à l'affichage
    
class ListingAdmin(admin.ModelAdmin):
    list_display=('title', 'groupe')

admin.site.register(Groupe, GroupeAdmin)
admin.site.register(Article, ListingAdmin)