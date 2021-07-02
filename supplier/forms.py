from django import forms
from .models import Supplier

class SuppliersForm(forms.ModelForm):
  # def clean_qq(self):
  #   cleaned_data = self.cleaned_data('qq')
  #   if not cleaned_data.isdigit():
  #     raise forms.ValidationError('必须是数字')
  #   return int(cleaned_data)  
  

  class Meta:
    model = Supplier
    fields = (
      'sp_name', 'address', 'c_person', 'c_phone'
    )
    dic = {}
    for field in fields:
      dic[field] = forms.TextInput(attrs={'class': 'form-control'})
    widgets = dic