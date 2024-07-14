from django import forms


class inversionf(forms.Form):
    fechaf = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'date', 'size': '9'}))
    montoinvf = forms.FloatField(widget=forms.TextInput(attrs={'size': '11'}))
