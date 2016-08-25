from django.contrib import admin

from pdp7_pt.measures import models


admin.site.register(models.Series)
admin.site.register(models.FloatMeasure)
admin.site.register(models.DoublePositiveIntegerMeasure)
