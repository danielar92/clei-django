from django import forms
from modulo_clei.models import CLEI, Topico, CP, Articulo, Inscripcion
from personas.models import Persona

class CLEIForm(forms.ModelForm):
    miembros = forms.ModelMultipleChoiceField(queryset=Persona.objects.all())

    def clean(self):

        cleaned = super(CLEIForm, self).clean()
        fechaInscripcion = cleaned.get('fechaInscripcion')
        fechaInscripcionDescuento = cleaned.get('fechaInscripcionDescuento')
        fechaTopeArticulo  = cleaned.get('fechaTopeArticulo')
        fechaNotificacion  = cleaned.get('fechaNotificacion')
        fechaInicio  = cleaned.get('fechaInicio')
        tarifaReducida = cleaned.get('tarifaReducida')
        tarifaNormal  = cleaned.get('tarifaNormal')
        if fechaInscripcion and fechaInscripcionDescuento and fechaInscripcion<fechaInscripcionDescuento:
            self._errors['fechaInscripcion'] = self.error_class(["La fecha de inscripcion con descuento debe ser antes que la fecha de inscripcion general"])
            del cleaned['fechaInscripcion']

        if fechaTopeArticulo and fechaInicio and fechaTopeArticulo>fechaInicio:
            self._errors['fechaTopeArticulo'] = self.error_class(["La fecha tope de articulos debe venir antes de la fecha de inicio"])
            del cleaned['fechaTopeArticulo']

        if fechaNotificacion and fechaInicio and fechaNotificacion>fechaInicio:
            self._errors['fechaNotificacion'] = self.error_class(["La fecha de notificacion de articulos debe venir antes de la fecha de inicio"])
            del cleaned['fechaNotificacion']

        if tarifaReducida and tarifaNormal and tarifaReducida>tarifaNormal:
            self._errors['tarifaReducida'] = self.error_class(["La tarifa reducida debe ser menor a la tarifa normal"])

            del cleaned['tarifaReducida']
        return cleaned

    class Meta:
        model = CLEI

class TopicoForm(forms.ModelForm):
    class Meta:
        model = Topico

class ArticuloForm(forms.ModelForm):
    def clean_pclaves(self):
        data = self.cleaned_data['pclaves']
        if len(data.split(',')) > 5:
            raise forms.ValidationError("A lo sumo debes especificar 5 palabras claves!")
        return data

    class Meta:
        model = Articulo
        exclude = ['clei', 'status']

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = []


# class CPForm(forms.ModelForm):
#     class Meta:
#         model = CP
