from django.contrib import admin

from pdp7_pt.measures import models


class MeasureAdmin(admin.ModelAdmin):
    date_hierarchy = 'when'


admin.site.register(models.Series)
admin.site.register(models.FloatMeasure, MeasureAdmin)
admin.site.register(models.DoublePositiveIntegerMeasure, MeasureAdmin)
