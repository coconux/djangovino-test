#from cave.models import Cave, Couleur,TypeBouteille,Classification,Bouteille
from django.db import models                                                                                                                                                     
from django.db.models import *                                                                                                                                                     



#Couleur
m,n = Couleur.objects.get_or_create(nom="Rosé",defaults={'nom':'Rosé'})
m,n = Couleur.objects.get_or_create(nom="Rouge",defaults={'nom':'Rouge'})
m,n = Couleur.objects.get_or_create(nom="Blanc",defaults={'nom':'Blanc'})

#TypeBouteille
m,n = TypeBouteille.objects.get_or_create(nom="Magnum",defaults={'nom':'Magnum','volume':'1,5L','ml':1500})
m,n = TypeBouteille.objects.get_or_create(nom="Double Magnum",defaults={'nom':'Double\
                                                            Magnum','volume':'3L','ml':3000})
m,n =TypeBouteille.objects.get_or_create(nom="75cl",defaults={'nom':'75cl','volume':'75cl','ml':750})
