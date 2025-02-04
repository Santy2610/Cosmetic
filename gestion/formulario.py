from django import forms
from gestion.models import promot


class vistvent(forms.Form):
    calef = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'date', 'size': '9'}))


class pedidof(forms.Form):
    descripf = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'size': '50'}))
    cantidf = forms.IntegerField()


class buspromt(forms.Form):
    lista = forms.ModelChoiceField(queryset=promot.objects.values_list(
        'nombre', flat=True).order_by('nombre'))  # type: ignore
