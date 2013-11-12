from django.conf.urls import patterns, url

from cave import views



urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^populate/', views.populate, name='populate'),
    url(r'^testcave/', views.testcave, name='testcave'),
    url(r'^home/', views.home, name='home'),
    url(r'^voirCave/', views.voirCave, name='voirCave'),
    url(r'^add_bouteille$', views.add_bouteille, name='add_bouteille'),
    url(r'^place_bouteille$', views.place_bouteille, name='place_bouteille'),

    #url(r'^$', views.TicketView, name='TicketView')
)
