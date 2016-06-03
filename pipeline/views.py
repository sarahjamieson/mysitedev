from django.shortcuts import render
import vcf
from pipeline.models import Results, ResultTable
import sqlite3 as lite
from pipeline.aml_pipeline import get_output


def index(request):
    items = []
    item_ids = []
    for item in Results.objects.all():
        if item.run not in item_ids:
            items.append(item)
            item_ids.append(item.run)
    return render(request, 'pipeline/index.html', {'runs': items})


def get_samples(request, run):
    items = []
    item_ids = []
    for item in Results.objects.filter(run__icontains=run):
        if item.sample not in item_ids:
            items.append(item)
            item_ids.append(item.sample)
    return render(request, 'pipeline/samples.html', {'samples': items})


def get_results(request, sample):
    result = ResultTable(Results.objects.filter(sample__icontains=sample))
    return render(request, 'pipeline/results.html', {'results': result})
