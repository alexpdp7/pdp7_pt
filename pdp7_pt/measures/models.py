from django.contrib.auth import models as auth_models
from django.contrib.contenttypes import models as contenttypes_models
from django.db import models


class Series(models.Model):
    name = models.CharField(max_length=100)
    measure_type = models.ForeignKey(contenttypes_models.ContentType)

    def __str__(self):
        return self.name


class Measure(models.Model):
    when = models.DateTimeField(auto_now_add=True)
    who = models.ForeignKey(auth_models.User)
    series = models.ForeignKey(Series)

    def __str__(self):
        return '{0} {1}'.format(self.series, self.when)


class FloatMeasure(Measure):
    value = models.FloatField()

    def __str__(self):
        return '{0}: {1}'.format(super(FloatMeasure, self).__str__(), self.value)


class DoublePositiveIntegerMeasure(Measure):
    value_1 = models.PositiveIntegerField()
    value_2 = models.PositiveIntegerField()

    def __str__(self):
        return '{0}: {1}-{2}'.format(super(DoublePositiveIntegerMeasure, self).__str__(), self.value_1, self.value_2)
