from django import forms
from .models import Compra, Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'marca': forms.Select(attrs={'class': 'form-select'}),
        }
        
        def clean_precio(self):
            precio=self.cleaned_data.get()
            if precio<0:
                raise forms.ValidationError('El precio no puede ser negativo')
            return precio
        

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['unidades']
        widgets = {
            'unidades': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'value': '1'}),
        }
    
    
    def clean_unidades(self):
        unidades = self.cleaned_data['unidades']
        if unidades < 1:
            raise forms.ValidationError("Debes comprar al menos una unidad.")
        return unidades