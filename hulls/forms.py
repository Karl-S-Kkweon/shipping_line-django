from django import forms
from django_countries.fields import CountryField


class SearchForm(forms.Form):

    name = forms.CharField(initial="Anything", required=False)
    country = CountryField().formfield(required=False)
    price = forms.IntegerField(required=False)
