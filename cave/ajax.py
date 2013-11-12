from django.utils import simplejson
from cave.models import Cave, Couleur,TypeBouteille,Classification,Bouteille,Annee,Cellule,Pays,Region,RefBouteille

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.views.decorators.csrf import csrf_exempt


import json
@dajaxice_register(method='GET')
def sayhello(request):
    b=Bouteille.objects.all()

    return simplejson.dumps({'message':'Hello World from python3.3'})



@csrf_exempt
@dajaxice_register(method='POST')
def testArg(request):

    dajax = Dajax()
    #result = dir(request)
    post = request.POST['argv']
    #result = request.POST['argv']
    list_bouteille = json.loads(post)

    for bouteille in list_bouteille:
        nom = bouteille[0]
        quantite = bouteille[1]
        print ("Une bouteille du nom de "+bouteille+ " et de quantité "+quantite)


    dajax.assign('#result','value',str(list_bouteille))
    return dajax.json()
    #return simplejson.dumps({'message':'Hello World from python3.3 %s'})

