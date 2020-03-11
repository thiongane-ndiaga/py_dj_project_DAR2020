"""tracking_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('inscription/',views.form_inscription,name='inscription'),
    path('connexion/' ,views.form_conn,name='connexion'),
    path('deconnexion/' ,views.deconnexion,name='deconnexion'),
    path('',views.liste_suivis,name='liste_suivis'),
    path('<slug:slug_suivi>',views.details_suivi,name='details_suivi'),
    path('ajout_suivi/',views.AjoutSuiviView.as_view(), name='ajout_suivi'),
    path('del_depense/<int:pk>',views.del_depense,name='del_depense'),
    path('del_suivi/<slug:slug_suivi>',views.del_suivi,name='del_suivi')
]
