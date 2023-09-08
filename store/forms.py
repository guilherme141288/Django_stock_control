from django import forms

from .models import Store


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store

        fields = ['name' , 'cnpj' , 'image' , 'address' , 'city' , 'state' ]

        widgets = {
            
            
            'name':forms.TextInput(attrs={'type':'text' , 'class':'form-control' , 'placeholder' : 'Nome da Loja' }) ,
            'cnpj':forms.TextInput(attrs={'type':'text' , 'class':'form-control' , 'placeholder' : 'CNPJ' }),
             
            'image':forms.FileInput(attrs={'type':'text' , 'class':'form-control' , 'placeholder' : 'Imagem' }),
            'address':forms.TextInput(attrs={'type':'text' , 'class':'form-control' , 'placeholder' : 'Endereço' }),
            'city':forms.TextInput(attrs={'type':'text' , 'class':'form-control' , 'placeholder' : 'Cidade' }),
            'state':forms.TextInput(attrs={'type':'text' , 'class':'form-control' , 'placeholder' : 'Estado' }),

        }