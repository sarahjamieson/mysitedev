from django import forms


class GeneSearchForm(forms.Form):
    gene = forms.CharField(max_length=10)
    refseq = forms.CharField(max_length=30)
