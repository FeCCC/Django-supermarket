from django import forms
from .models import Purchase
from django.core.exceptions import ValidationError


class PurchaseForm(forms.ModelForm):
    def clean_p_price(self):
        data = self.cleaned_data['p_price']
        if data <= 0:
            raise ValidationError('确保该值大于0')
        return data

    class Meta:
        model = Purchase
        fields = (
            'g_id', 'p_num', 'st_id', 'p_price', 'sp_id'
        )
        dic = {}
        for field in fields:
            dic[field] = forms.TextInput(attrs={'class': 'form-control'})
        widgets = dic
