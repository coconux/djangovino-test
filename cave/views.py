# -*- coding: utf-8 -*-
import json
from django.shortcuts import render_to_response
from django.http import HttpResponse
from cave.models import Cave, Couleur,TypeBouteille,Classification,Bouteille,Annee,Cellule,Pays,Region,RefBouteille
from datetime import datetime

from django.views.decorators.csrf import csrf_exempt


#[ Cellule.objects.get_or_create(cave=c,x=1,y=1, defaults={'cave':c,'x':1,'y':w[1]})  for int(w) in range (0,len(A),1)]

def testcave(request):
   return render_to_response('html/cave/dnd.html')

def home(request):
   return render_to_response('html/cave/home.html')

   return HttpResponse("hello")


@csrf_exempt
def place_bouteille(request):
    # recuperation de la liste des bouteille
    post = request.POST['list_bouteille']
    # le post est au format json. On le désérialize
    list_bouteille = json.loads(post)
    # on affiche chaque élément. Ici vous devez faire votre traitement, une insertion
    # en base de données par exemple
    for bouteille in list_bouteille:
        nom = bouteille['nom']
        id = bouteille['id']
        id_cave = bouteille['id_cave']
        x = bouteille['x']
        y = bouteille['y']
        print ("Placement de "+id+"("+nom+") dans la cave:"+id_cave+" sur ligne:"+x+"colonne:"+y)

    #On recupere la bouteille en base
    b=Bouteille.objects.get(id=id)
    #ON recupere la cellule en base
    cell=Cellule.objects.get(cave=Cave.objects.get(id=id_cave),x=x,y=y)
    #On place la bouteille
    b.place(cell)



    # on fait un retour au client
    json_data = json.dumps({"HTTPRESPONSE":"ok"})
    # json data est maintenant au format JSON et pret à etre envoyé au client
    return HttpResponse(json_data, mimetype="application/json")

@csrf_exempt
def add_bouteille(request):
    # recuperation de la liste des bouteille
    post = request.POST['list_bouteille']
    # le post est au format json. On le désérialize
    list_bouteille = json.loads(post)
    # on affiche chaque élément. Ici vous devez faire votre traitement, une insertion
    # en base de données par exemple
    for bouteille in list_bouteille:
        nom = bouteille['nom']
        quantite = bouteille['quantite']
        print ("Une bouteille du nom de "+nom+ " et de quantité "+str(quantite))
    # on fait un retour au client
    json_data = json.dumps({"HTTPRESPONSE":"ok"})
    # json data est maintenant au format JSON et pret à etre envoyé au client
    return HttpResponse(json_data, mimetype="application/json")


def voirCave(request):
    c = Cave.objects.all()[1]
    b=Bouteille.objects.all()

    cellOcc=[b for b in c.mesCellules.select_related() if b.occupe is True]

    return render_to_response('html/cave/voirCave.html',{'cave': c, 'bouteilles':b, 'cellules':cellOcc, 'lignes':range(c.lignes), 'colonnes':range(c.colonnes) })

def populate(request):
   #return render_to_response('home.html', {"foo": "bar"})

    #Annee
    [Annee.objects.get_or_create(nom=str(b),defaults={'nom':str(b),'annee':str(b)+'-01-01'}) for b in range(1800,2050,1)]

    #Cave
    m,n = Cave.objects.get_or_create(nom="CocoVino",defaults={'nom':'CocoVino'})
   
    #Couleur
    m,n = Couleur.objects.get_or_create(nom="Rosé",defaults={'nom':'Rosé'})
    m,n = Couleur.objects.get_or_create(nom="Rouge",defaults={'nom':'Rouge'})
    m,n = Couleur.objects.get_or_create(nom="Blanc",defaults={'nom':'Blanc'})

    #TypeBouteille
    m,n = TypeBouteille.objects.get_or_create(nom="Magnum",defaults={'nom':'Magnum','volume':'1,5L','ml':1500})
    m,n = TypeBouteille.objects.get_or_create(nom="Double Magnum",defaults={'nom':'Double Magnum','volume':'3L','ml':3000})
    m,n =TypeBouteille.objects.get_or_create(nom="75cl",defaults={'nom':'75cl','volume':'75cl','ml':750})

    #Classification
    m,n = Classification.objects.get_or_create(nom="Grand Cru",defaults={'nom':'Grand Cru'})
    m,n = Classification.objects.get_or_create(nom="Cru Artisan",defaults={'nom':'Cru Artisan'})
    
    #Pays
    m,n = Pays.objects.get_or_create(nom="Argentine",defaults={'nom':'Argentine'})
    m,n = Pays.objects.get_or_create(nom="France",defaults={'nom':'France'})
    
    #Region
    o,p = Region.objects.get_or_create(paysR=m,nom="Alsace",defaults={'paysR':m,'nom':'Alsace'})
    o,p = Region.objects.get_or_create(paysR=m,nom="Bordeaux",defaults={'paysR':m,'nom':'Bordeaux'})
    
    #Cellule
    c = Cave.objects.get(nom="CocoVino")
    A =[(x, y) for x in [xx for xx in range(0,c.colonnes,1)] for y in [yy for yy in range (0,c.lignes,1)] ]
    [ Cellule.objects.get_or_create(cave=c,x=A[X][0],y=A[X][1], defaults={'cave':c,'x':A[X][0],'y':A[X][1]})  for X in range (0,len(A),1)]


    #RefBouteille
    ref,ref2 = RefBouteille.objects.get_or_create(nomB="Bouteille 1",defaults={'nomB':'BouteilleRef 1','couleurB':Couleur.objects.get(nom='Rosé'),\
                                                                      'typeB':TypeBouteille.objects.get(nom='75cl'),\
                                                                      #'celluleB':Cellule.objects.get(cave=c,x=0,y=0),\
                                                                      'anneeB':Annee.objects.get(nom='2009')
                                                                     })
    ref,ref2 = RefBouteille.objects.get_or_create(nomB="Bouteille 2",defaults={'nomB':'BouteilleRef 2','couleurB':Couleur.objects.get(nom='Rouge'),\
                                                                      'typeB':TypeBouteille.objects.get(nom='75cl'),\
                                                                      #'celluleB':Cellule.objects.get(cave=c,x=0,y=0),\
                                                                      'anneeB':Annee.objects.get(nom='2005')
                                                                     })

    #Bouteille

    """  m,n = Bouteille.objects.get_or_create(nomB="Bouteille 1",defaults={'nomB':'Bouteille 1','couleurB':Couleur.objects.get(nom='Rosé'),\
                                                                      'typeB':TypeBouteille.objects.get(nom='75cl'),\
                                                                      'gardeMinB':Annee.objects.get(nom='2012'),\
                                                                      'gardeMaxB':Annee.objects.get(nom='2020'),\
                                                                      'prixB':'17',\
                                                                      #'celluleB':Cellule.objects.get(cave=c,x=0,y=0),\
                                                                      'anneeB':Annee.objects.get(nom='2009')
                                                                     })
    o,p = Bouteille.objects.get_or_create(nomB="Bouteille 2",defaults={'nomB':'Bouteille 2','couleurB':Couleur.objects.get(nom='Rouge'),\
                                                                      'typeB':TypeBouteille.objects.get(nom='75cl'),\
                                                                      'gardeMinB':Annee.objects.get(nom='2010'),\
                                                                      'gardeMaxB':Annee.objects.get(nom='2015'),\
                                                                      'prixB':'12',\
                                                                      #'celluleB':Cellule.objects.get(cave=c,x=0,y=1),\
                                                                      'anneeB':Annee.objects.get(nom='2008')

                                                                  })

    """
    # On met a jour les emplacements
    """emp = Cellule.objects.get(cave=c,x=0,y=0)
    emp2 = Cellule.objects.get(cave=c,x=1,y=1)
    m.place(emp)
    o.place(emp2)
    m.libere()
    """

    bigcave,n = Cave.objects.get_or_create(nom="Bigcave",defaults={'nom':'Bigcave',\
                                           'lignes':10,\
                                           'colonnes':10})
                                           

    return HttpResponse("populate")



