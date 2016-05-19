from django.shortcuts import render
from search import GeneSearch
from forms import GeneSearchForm


def gene_search(request):
    if request.method == 'POST':
        form = GeneSearchForm(request.POST)
        if form.is_valid():
            gene = form.cleaned_data['gene']
            refseq = form.cleaned_data['refseq']
            gsearch = GeneSearch(gene, refseq)
            ensg, lrg = gsearch.get_gene_info()
            transcript, protein = gsearch.get_transcript(ensg)
            return render(request, 'genesearch/search_result.html',
                          {'gene': gene, 'refseq': refseq, 'ensg': ensg, 'lrg': lrg, 'transcript': transcript,
                           'protein': protein})
    else:
        form = GeneSearchForm()
    return render(request, 'genesearch/search_form.html', {'form': form})

