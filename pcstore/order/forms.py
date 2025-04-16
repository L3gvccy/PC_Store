from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_type', 'post_company']
        widgets = {
            'delivery_type': forms.RadioSelect(),
            'post_company': forms.Select()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.fields['delivery_type'].choices[0][0] == '':
            self.fields['delivery_type'].choices = self.fields['delivery_type'].choices[1:]

        if self.fields['post_company'].choices[0][0] == '':
            self.fields['post_company'].choices = self.fields['post_company'].choices[1:]

        self.fields['delivery_type'].label = "Спосіб доставки"
        self.fields['post_company'].label = "Компанія доставки (для пошти)"
