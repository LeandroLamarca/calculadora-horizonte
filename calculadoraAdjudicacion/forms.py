from django.forms import ModelForm
from django import forms
from calculadoraAdjudicacion.models import PlanActual, PlanPorAdjudicar

class PlanActualForm (ModelForm):
    class Meta:
        model = PlanActual
        exclude = ['deuda']

class PlanPorAdjudicarForm(ModelForm):
    class Meta:
        model = PlanPorAdjudicar
        fields = '__all__'

class AporteActualForm(forms.Form):
    aporte_actual = forms.DecimalField(
        # label='Aporte mensual (antes de adjudicar)',
        # help_text='Monto mensual a aportar hasta el momento de la adjudicación',
        min_value=1,
        max_digits=8,
        decimal_places=2
        )