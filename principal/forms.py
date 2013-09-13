#encoding:utf-8
from django.forms import ModelForm
from principal.models import Grados, Grupos

class GradoForm(ModelForm):
    class Meta:
        model = Grados
        # fields = ['name', 'description', 'is_active']

class GrupoForm(ModelForm):
    class Meta:
        model = Grupos
        # fields = ['name', 'description', 'is_active']