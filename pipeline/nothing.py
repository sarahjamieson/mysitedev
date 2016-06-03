import vcf
from pipeline.models import Results, ResultTable
import os
import django


def random_function():
    vcf_reader = vcf.Reader(open('04-.annovar.vcf', 'r'))
    sample_no = vcf_reader.samples

    for record in vcf_reader:
        for sample in record:
            # PyVCF reader
            chr = record.CHROM
            pos = record.POS
            ref = record.REF
            alt = ",".join(str(a) for a in record.ALT)
            gt = sample['GT']
            ad = sample['AD']
            info_dict = record.INFO
            end_pos = info_dict.get("END")
            print end_pos
            sv_type = info_dict.get("SVTYPE")
            gene = ",".join(str(g) for g in info_dict.get("Gene.refGene"))
            func = ",".join(str(f) for f in info_dict.get("Func.refGene"))
            exonic_func = ",".join(str(f) for f in info_dict.get("ExonicFunc.refGene"))
            # hgvs
            ref_reads = ad[0]
            alt_reads = ad[1]
            total_reads = ref_reads + alt_reads
            if alt_reads != 0 and ref_reads != 0:
                ab = int((float(alt_reads) / float(ref_reads)) * 100)
            else:
                ab = int(0)
            size = info_dict.get("SVLEN")
            ad_str = '%s,%s' % (str(ref_reads), str(alt_reads))
