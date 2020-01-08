from django import forms

class CheckTT(forms.Form):
    """docstring for checktt"""
    thuoc_1 = forms.CharField(label='Thuoc 1', max_length=200)
    thuoc_2 = forms.CharField(label='Thuoc 2', max_length=200)
