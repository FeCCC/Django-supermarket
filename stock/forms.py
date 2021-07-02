from django import forms
from .models import Stock

class StocksForm(forms.ModelForm):
  # def clean_qq(self):
  #   cleaned_data = self.cleaned_data('qq')
  #   if not cleaned_data.isdigit():
  #     raise forms.ValidationError('必须是数字')
  #   return int(cleaned_data)  
  

  class Meta:
    model = Stock
    fields = (
      'g_id', 's_num', 'sp_id'
    )
    dic = {}
    for field in fields:
      dic[field] = forms.TextInput(attrs={'class': 'form-control'})
    widgets = dic