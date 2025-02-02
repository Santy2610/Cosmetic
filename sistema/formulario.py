from django import forms


class promtf(forms.Form):
    NombF = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'size': '30'}))
