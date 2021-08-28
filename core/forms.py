from django import forms

class NumForm(forms.Form):
    Number = forms.IntegerField()