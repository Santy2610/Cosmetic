from django import forms


class vistvent(forms.Form):
    calef = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'date', 'size': '9'}))


class pedidof(forms.Form):
    descripf = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'size': '50'}))
    cantidf = forms.IntegerField()
