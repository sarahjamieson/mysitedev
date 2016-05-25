from __future__ import unicode_literals

from django.db import models
import django_tables2 as table


class Results(models.Model):
    sampleid = models.AutoField(primary_key=True, unique=True)
    sample = models.CharField(max_length=30)
    chr = models.CharField(max_length=6)
    pos = models.CharField(max_length=30)
    ref = models.CharField(max_length=2)
    alt = models.CharField(max_length=2)
    type = models.CharField(max_length=10)
    gq = models.CharField(max_length=10)
    gene = models.CharField(max_length=10)


class ResultTable(table.Table):
    sample = table.Column(verbose_name="SAMPLE", orderable=False, default='')
    chr = table.Column(verbose_name="CHROM", orderable=False, default='')
    pos = table.Column(verbose_name="POS", orderable=False, default='')
    ref = table.Column(verbose_name="REF", orderable=False, default='')
    alt = table.Column(verbose_name="ALT", orderable=False, default='')
    type = table.Column(verbose_name="TYPE", orderable=False, default='')
    gq = table.Column(verbose_name="GQ", orderable=False, default='')
    gene = table.Column(verbose_name="GENE", orderable=False, default='')

    class Meta:
        model = Results
        fields = ('sample', 'chr', 'pos', 'ref', 'alt', 'type', 'gq', 'gene')
