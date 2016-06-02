from django.shortcuts import render
import vcf
from pipeline.models import Results, ResultTable
import sqlite3 as lite
from pipeline.aml_pipeline import get_output


def index(request):
    print "getting data from model table"
    result = ResultTable(Results.objects.all())
    return render(request, 'pipeline/index.html', {'results': result})
