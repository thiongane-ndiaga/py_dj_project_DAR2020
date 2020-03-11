from django import forms
from django.http import HttpResponseRedirect
from django.utils.text import slugify

class DepenseForm(forms.Form):
    titre = forms.CharField()
    montant = forms.IntegerField()
    new_cate = forms.CharField()
