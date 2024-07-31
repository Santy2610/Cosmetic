from django import forms


class inversionf(forms.Form):
    fechaf = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'date', 'size': '9'}))
    montoinvf = forms.FloatField(widget=forms.TextInput(attrs={'size': '11'}))


class almacenf(forms.Form):
    descripcionf = forms.CharField()
    presiocf = forms.FloatField(widget=forms.TextInput(attrs={'size': '9'}))
    presiobf = forms.FloatField(widget=forms.TextInput(attrs={'size': '9'}))
    cantidadf = forms.IntegerField(
        widget=forms.TextInput(attrs={'size': '5'}))
