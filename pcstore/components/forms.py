from django import forms

class CPUFilterForm(forms.Form):
    name = forms.CharField(required=False, label='Пошук по назві')
    brand = forms.CharField(required=False, label='Виробник')
    socket = forms.CharField(required=False, label='Сокет')
    min_cores = forms.IntegerField(required=False, label='Мін. ядра')
    min_price = forms.DecimalField(required=False, label='Мін. ціна')
    max_price = forms.DecimalField(required=False, label='Макс. ціна')