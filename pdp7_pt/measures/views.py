from django.contrib.auth.decorators import login_required
from django import forms
from django import shortcuts

from pdp7_pt.measures import forms as measures_forms
from pdp7_pt.measures import models


@login_required
def index(request):
    if request.method == 'POST':
        form = measures_forms.ChooseSeriesForm(request.POST)
        return shortcuts.redirect('measurement', series=form.data['series'])
    else:
        form = measures_forms.ChooseSeriesForm()
    return shortcuts.render(request, 'measures/index.html', {'form': form})


@login_required
def measurement(request, series):
    series = models.Series.objects.get(pk=series)
    model = series.measure_type.model_class()
    form_class = forms.modelform_factory(model, exclude=['when', 'who', 'series'])
    if request.method == 'POST':
        form = form_class(request.POST)
        measurement = form.save(commit=False)
        measurement.who = request.user
        measurement.series = series
        measurement.save()
        return shortcuts.redirect('index')
    form = form_class()
    return shortcuts.render(request, 'measures/measurement.html', {'form': form})
