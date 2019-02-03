from django.forms import ModelForm,inlineformset_factory
from django import forms
from . import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from . import middleware

#user = middleware.get_current_user()

class CrearProyecto(ModelForm):
    class Meta:
        model = models.proyecto
        fields = ['folio','tomo','numero_instrumento','enajenante','adquirente','localizacion',
        'tipo','slug']
        widgets ={
            "folio":forms.TextInput(attrs={'class': 'form-control','placeholder': ''}),
            "tomo":forms.TextInput(attrs={'class': 'form-control','placeholder': ''}),
            "numero_instrumento":forms.TextInput(attrs={'class': 'form-control','placeholder': ''}),
            "enajenante":forms.TextInput(attrs={'class': 'form-control','placeholder': ''}),
            "adquirente":forms.TextInput(attrs={'class': 'form-control','placeholder': ''}),
            "localizacion":forms.TextInput(attrs={'class': 'form-control','placeholder': ''}),
            "tipo":forms.TextInput(attrs={'class': 'form-control','placeholder': ''}),
            "slug":forms.HiddenInput()
        }
class AgregarProgreso(ModelForm):
    class Meta:
        model = models.progreso
        fields = ['id_proyecto','titulo','description']
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(AgregarProgreso,self).__init__( *args, **kwargs)
        self.fields['id_proyecto'].label = "Proyecto"
        self.fields['id_proyecto'].widget.attrs['class'] = 'form-control'
        self.fields['description'].label = "Describir"
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['titulo'].label = "Titulo"
        self.fields['titulo'].widget.attrs['class'] = 'form-control'
        self.fields['id_proyecto'].queryset = models.proyecto.objects.filter(autor_id=user)
class GuardarProgreso(ModelForm):
    class Meta:
        models.progreso
        fields: ['estado']
    def __init__(self, *args, **kwargs):
        super(AgregarProgreso,self).__init__( *args, **kwargs)
        self.fields['estado'].label = "Estado"
        self.fields['estado'].widget.attrs['class'] = 'control-inline fancy-checkbox'
class EditarProyecto(ModelForm):
    class Meta:
        model = models.proyecto
        fields = ["tomo","numero_instrumento","enajenante","adquirente","localizacion","tipo"]
    def __init__(self, *args, **kwargs):
        super(EditarProyecto,self).__init__( *args, **kwargs)
        self.fields['tomo'].label = "Tomo"
        self.fields['tomo'].widget.attrs['class'] = 'form-control'
        self.fields['tomo'].widget.attrs['placeholder'] = 'self'
        self.fields['numero_instrumento'].label = "Número de Instrumento"
        self.fields['numero_instrumento'].widget.attrs['class'] = 'form-control'
        self.fields['enajenante'].label = "Enajenante"
        self.fields['enajenante'].widget.attrs['class'] = 'form-control'
        self.fields['adquirente'].label = "Adquirente"
        self.fields['adquirente'].widget.attrs['class'] = 'form-control'
        self.fields['localizacion'].label = "Localizacion"
        self.fields['localizacion'].widget.attrs['class'] = 'form-control'
