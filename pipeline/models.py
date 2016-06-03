from __future__ import unicode_literals

from django.db import models
import django_tables2 as table


class Results(models.Model):
    sample_id = models.AutoField(primary_key=True, unique=True)
    run = models.CharField(max_length=100, default='')
    sample = models.CharField(max_length=30)
    caller = models.CharField(max_length=10)
    chr = models.CharField(max_length=6)
    pos = models.IntegerField()
    ref = models.CharField(max_length=2)
    alt = models.CharField(max_length=2)
    end_pos = models.IntegerField()
    sv_type = models.CharField(max_length=10, default='')
    size = models.IntegerField()
    gt = models.CharField(max_length=5, default='')
    total_reads = models.IntegerField()
    ad = models.CharField(max_length=5, default='')
    ab = models.IntegerField()
    gene = models.CharField(max_length=10)
    func = models.CharField(max_length=300, default='')
    exonic_func = models.CharField(max_length=300, default='')

    class Meta:
        app_label = 'pipeline'
        db_table = 'Results'


class ResultTable(table.Table):
    sample = table.Column(verbose_name="SAMPLE", orderable=False, default='')
    caller = table.Column(verbose_name="CALLER", orderable=False, default='')
    chr = table.Column(verbose_name="CHROM", orderable=False, default='')
    pos = table.Column(verbose_name="POS", orderable=False, default='')
    ref = table.Column(verbose_name="REF", orderable=False, default='')
    alt = table.Column(verbose_name="ALT", orderable=False, default='')
    end_pos = table.Column(verbose_name="END", orderable=False, default='')
    sv_type = table.Column(verbose_name="TYPE", orderable=False, default='')
    size = table.Column(verbose_name="SIZE", orderable=False, default='')
    gt = table.Column(verbose_name="GT", orderable=False, default='')
    total_reads = table.Column(verbose_name="DEPTH", orderable=False, default='')
    ad = table.Column(verbose_name="AD", orderable=False, default='')
    ab = table.Column(verbose_name="AB", orderable=False, default='')
    gene = table.Column(verbose_name="GENE", orderable=False, default='')
    func = table.Column(verbose_name="FUNC.refGENE", orderable=False, default='')
    exonic_func = table.Column(verbose_name="EXONICFUNC.refGENE", orderable=False, default='')

    class Meta:
        model = Results
        fields = ('sample', 'caller', 'chr', 'pos', 'ref', 'alt', 'end_pos', 'sv_type', 'size', 'gt', 'total_reads',
                  'ad', 'gene', 'func', 'exonic_func')
