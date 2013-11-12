# -*- coding: utf-8 -*-
from django.contrib import admin
from cave.models import Cave, Couleur,TypeBouteille,Classification,Bouteille,Annee,Cellule,Pays,Region,RefBouteille

admin.site.register(Cave)
admin.site.register(Couleur)
admin.site.register(TypeBouteille)
admin.site.register(Classification)
admin.site.register(Bouteille)
admin.site.register(Annee)
admin.site.register(Cellule)
admin.site.register(Pays)
admin.site.register(Region)
admin.site.register(RefBouteille)
