from urllib2 import urlopen
import json
from biomart import BiomartServer


class GeneSearch(object):
    def __init__(self, gene, refseq):
        self.gene = gene
        self.refseq = refseq

    def get_gene_info(self):
        """Takes a gene and uses Ensembl API (GET xrefs/symbol/:species/:symbol) to extract ENSG and LRG codes.

        :param gene: gene to be searched for.
        :return: ENSG and LRG codes.
        """
        # 1) Connect to webpage with details for specified gene.
        webpage = urlopen("http://rest.ensembl.org/xrefs/symbol/homo_sapiens/%s?content-type=application/json"
                          % self.gene)
        # 2) Read webpage to see results.
        result = webpage.read()
        # 3) Use JSON to put results into a dictionary.
        jdata = json.loads(result)
        gene_list = []
        # 4) Iterate through dict to get matching keys and values. We want key="id" for ensg and lrg codes. Add to list.
        for item in jdata:
            for key, value in item.iteritems():
                if key == "id":
                    gene_list.append(value)
        ensg = gene_list[0]
        lrg = gene_list[1]

        return ensg, lrg

    def get_transcript(self, ensg):
        """Takes ENSG and RefSeq codes to find Ensembl transcript ID and peptide ID.

        :param ensg: ENSG number.
        :param refseq: RefSeq NM_ code.
        :return: transcript and protein IDs.
        """
        # 1) Connect to BioMart server.
        server = BiomartServer("http://www.ensembl.org/biomart")
        server.verbose = True  # provides setting up details
        new_list = []
        # 2) Select dataset to check against. Not essential but quicker so BioMart doesn't need to search.
        hs_genes = server.datasets['hsapiens_gene_ensembl']
        # 3) This is like clicking Results on the BioMart website. Filter by ENSG and RefSeq to get transcript & peptide
        results = hs_genes.search({
            'filters': {'ensembl_gene_id': '%s' % ensg,
                        'refseq_mrna': '%s' % self.refseq},
            'attributes': ['ensembl_transcript_id', 'ensembl_peptide_id']
        }, header=1)
        # 4) Convert to readable format and add relevant information to a list.
        for line in results.iter_lines():
            line = line.decode('utf-8')
            new_list.append(line.split())
        uni_transcript = new_list[1]
        transcript = uni_transcript[0]
        protein = uni_transcript[1]

        return transcript, protein
