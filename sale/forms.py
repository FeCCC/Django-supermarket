from django import forms
from django.core.exceptions import ValidationError
from .models import Sale


class SalesForm(forms.ModelForm):
    def clean_s_price(self):
        data = self.cleaned_data['s_price']
        if data <= 0:
            raise ValidationError('确保该值大于0')
        return data

    class Meta:
        model = Sale
        fields = (
            'g_id', 's_num', 'st_id', 's_price',
        )
        dic = {}
        for field in fields:
            dic[field] = forms.TextInput(attrs={'class': 'form-control'})
        widgets = dic
