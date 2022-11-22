from django import forms
from django.forms import ValidationError
#para el mapa
from .models import Search, Noticia

def solo_caracteres(valor):
    if any(char.isdigit() for char in valor):
        raise ValidationError('El campo no puede contener números. %(valor)s',
                                code='Error1',
                                params={'valor':valor}
                                )

class ContactoForm(forms.Form):

    TIPO_CONSULTA = (
        ("",'-Seleccione-'),
        (2,'Pediatría'),
        (3,'Traumatología'),
        (4,'Odontología'),
    )
    
    nombre = forms.CharField(
            label='Nombre',
            max_length=50,
            required=False,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'})
        )
    apellido = forms.CharField(
            label='Apellido',
            max_length=50,
            required=False,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Apellido'})
        )
    dni = forms.CharField(
            label='DNI',
            max_length=50,
            required=False,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'DNI'})
        )            
    email = forms.EmailField(
            label='Email',
            max_length=150,
            error_messages={
                'required':'Por favor completa el email'
            },
            widget=forms.TextInput(attrs={'class':'form-control','type':'email','placeholder':'email'})
        )
    direccion = forms.CharField(
            label='Direccion',
            max_length=100,
            widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección'})
        )
    localidad = forms.CharField(
            label='Localidad',
            max_length=50,
            required=False,
            validators=(solo_caracteres,),
            widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Localidad'})
        )        
    mensaje = forms.CharField(
            label='Mensaje',
            max_length=500,
            widget=forms.Textarea(attrs={'class':'form-control','rows':5, 'placeholder':'Detalle aquí el motivo de su consulta'})
        )
    suscripcion = forms.BooleanField(
        label='Deseo suscribirme al newsletter de DJ Hospital',
        required=False,
        widget=forms.CheckboxInput(attrs={'class':'form-check-input','value':1})
    )

    tipo_consulta = forms.ChoiceField(
        label='Tipo de consulta',
        choices=TIPO_CONSULTA,
        initial='',
        widget=forms.Select(attrs={'class':'form-control'})
    )


    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 15:
            raise ValidationError('Tu mensaje debe ser mayor a 15 caracteres')
        return data

    def clean_asunto(self):
        data = self.cleaned_data['asunto']
        return 'Asunto-'+data

    
    def clean(self):
        cleaned_data = super().clean()
        asunto = cleaned_data.get("asunto")
        suscripcion = cleaned_data.get("suscripcion")


        if suscripcion and asunto and "suscripcion" not in asunto:
            msg = "Debe agregar la palabara 'suscripcion' al asunto."
            self.add_error('asunto', msg)

#para el mapa
class SearchForm(forms.ModelForm):
    address = forms.CharField(label='')

    class Meta:
        model = Search
        fields = ['address', ]

#noticias
from django import forms



class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ('title', 'text',)
        
