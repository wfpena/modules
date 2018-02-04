# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

PERIOD = (
    ('0', 'Diário'),
    ('1', 'Semanal'),
    ('2', 'Mensal'),
    ('3', 'Anual'),
)

class ExampleModel(models.Model):
    titulo = models.CharField(max_length=255)
    period = models.CharField(max_length=1, choices=PERIOD)

    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = _('Example')
        verbose_name_plural = _('Examples')
