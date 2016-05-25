from django.shortcuts import render
import vcf
from django.db import models
from pipeline.models import Results, ResultTable
import os
import django


def get_output(vcf_file):
    print "performing get_output"
    sample = vcf_file[:-12]
    vcf_reader = vcf.Reader(open(vcf_file, 'r'))
    for record in vcf_reader:
        # PyVCF reader
        chr = record.CHROM
        pos = record.POS
        ref = record.REF
        alt = ",".join(str(a) for a in record.ALT)
        type = record.var_type
        # for sample in record.samples:
            # gt = sample['GT']

        if record.QUAL is None:
            gq = '.'
        else:
            gq = record.QUAL

        # ANNOVAR info
        info_dict = record.INFO
        gene = ",".join(str(g) for g in info_dict.get("Gene.refGene"))
        print "completed annovar getting, now putting into results model"
        result = Results.objects.update_or_create(sample=sample, chr=chr, pos=pos, ref=ref, alt=alt, type=type, gq=gq,
                                                  gene=gene)
        result.save()


def index(request):
    # get_output('cataracts.annovar.vcf')
    print "getting data from model table"
    result = ResultTable(Results.objects.all())
    return render(request, 'pipeline/index.html', {'results': result})

