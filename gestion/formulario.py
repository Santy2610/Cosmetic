from django import forms


class vistvent(forms.Form):
    calef = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'date', 'size': '9'}))
