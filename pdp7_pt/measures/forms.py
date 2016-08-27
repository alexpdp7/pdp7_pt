from django import forms

from pdp7_pt.measures import models


class ChooseSeriesForm(forms.Form):
    series = forms.ModelChoiceField(queryset=models.Series.objects.all())
