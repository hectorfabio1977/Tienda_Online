from django import forms
from Proveedores.models import Departamento

class Proveedoresform(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'
