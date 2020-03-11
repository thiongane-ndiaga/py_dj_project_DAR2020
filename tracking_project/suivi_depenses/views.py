from django.shortcuts import get_object_or_404, redirect, render
from .models import Suivi, Categorie, Depense
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.text import slugify
from django import forms
from .forms import DepenseForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


# Create your views here.
def form_inscription(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return render(request,"suivi_depenses/liste_suivis.html",{'user':user})

    form = UserCreationForm()
    return render(request,'suivi_depenses/form_inscription.html',{'form':form})

def form_conn(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return HttpResponseRedirect("/")
    form=AuthenticationForm()
    return render(request,'suivi_depenses/form_connexion.html',{'form':form})

def deconnexion(request):
    if request.method=='POST':
        logout(request)
        return HttpResponseRedirect("/connexion/")

@login_required(login_url="/connexion/")
def liste_suivis(request):
    user=request.user
    suivis=Suivi.objects.filter(user=user)
    return render(request,'suivi_depenses/liste_suivis.html',{'suivis':suivis})

@login_required(login_url="/connexion/")
def details_suivi(request,slug_suivi):
    suivi = get_object_or_404(Suivi, slug=slug_suivi)
    categories = Categorie.objects.all()
    if request.method == 'GET':
        return render(request,'suivi_depenses/details_suivi.html',{'suivi':suivi,'depenses':suivi.depenses.all(),'categories':categories})
    elif request.method=='POST':
        form = DepenseForm(request.POST)
        if form.is_valid():
            titre = form.cleaned_data['titre']
            montant = form.cleaned_data['montant']
            nom_cate = form.cleaned_data['new_cate'].title()
            same = False
            for c in categories:
                if c.nom==nom_cate:
                    same=True
            if same==False:
                Categorie.objects.create(nom=nom_cate).save()

            categorie=Categorie.objects.get(nom=nom_cate)
            Depense.objects.create(
                suivi = suivi,
                titre = titre,
                montant = montant,
                categorie = categorie
            ).save()
    
    return HttpResponseRedirect("/"+slug_suivi)    

@login_required(login_url="/connexion/")           
def del_depense(request,pk):
    d = Depense.objects.get(pk=pk)
    suivi=d.suivi
    d.delete()
    return HttpResponseRedirect("/"+suivi.slug)

@login_required(login_url="/connexion/")
def del_suivi(request,slug_suivi):
    s = Suivi.objects.get(slug=slug_suivi)
    s.delete()
    return HttpResponseRedirect("/")

class AjoutSuiviView(LoginRequiredMixin,CreateView):
    login_url = '/connexion/'
    model = Suivi
    template_name = 'suivi_depenses/ajout_suivi.html'
    fields = ('nom', 'budget' , 'date_limite')

    def form_valid(self, form):
        user=self.request.user
        self.object = form.save(commit=False)
        self.object.user=user
        self.object.save()

        return HttpResponseRedirect("/"+self.get_success_url())

    def get_success_url(self):
        return slugify(self.request.POST['nom'])
