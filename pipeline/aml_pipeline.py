import vcf
import sqlite3 as lite


def get_output(vcf_file):
    vcf_reader = vcf.Reader(open(vcf_file, 'r'))
    sample_no = vcf_reader.samples[0]

    con = lite.connect('/home/cuser/PycharmProjects/django_apps/mysitedev/primers.db.sqlite3')
    curs = con.cursor()
    curs.execute("DROP TABLE IF EXISTS Results")
    curs.execute("CREATE TABLE IF NOT EXISTS Results(sample_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, sample TEXT,"
                 " caller TEXT, chr TEXT, pos INTEGER, ref TEXT, alt TEXT, end_pos INTEGER, sv_type TEXT, size INTEGER,"
                 " gt TEXT, total_reads INTEGER, ad TEXT, ab INTEGER, gene TEXT, func TEXT, exonic_func TEXT)")

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

            curs.execute("INSERT INTO Results (sample, caller, chr, pos, ref, alt, end_pos, sv_type, size, gt, "
                         "total_reads, ad, ab, gene, func, exonic_func) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                         (sample_no, 'Pindel', chr, pos, ref, alt, end_pos, sv_type, size, gt, total_reads, ad_str,
                          ab, gene, func, exonic_func))
            con.commit()