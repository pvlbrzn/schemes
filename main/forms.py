from django import forms
from .models import Schema, Column
from django.forms import inlineformset_factory


class SchemaForm(forms.ModelForm):
    class Meta:
        model = Schema
        fields = ['name']


ColumnFormSet = inlineformset_factory(
    Schema,
    Column,
    fields=('name', 'data_type', 'order'),
    extra=1,
    can_delete=True
)
