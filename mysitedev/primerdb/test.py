import sqlite3 as lite
import pandas as pd
import os


class SeeChanges(object):
    def __init__(self, df, gene):
        self.df = df
        self.gene = gene
        global con, curs
        con = lite.connect(os.path.join(os.pardir, 'primers.db.sqlite3'))
        curs = con.cursor()

    def check_changes(self):
        n = 0
        query = "SELECT * FROM Primers WHERE Gene LIKE 'COL4A5'"
        df_sql = pd.read_sql_query(query, con=con)
        for row_index, row in self.df.iterrows():
            if str(row['Gene']) == str(df_sql.get_value(n, 'Gene')):
                n += 1
                print "new value matches old value"
            else:
                print "value changed from %s to %s" % str(row['Gene']), str(df_sql.get_value(n, 'Gene'))

    #  primertable new = df
    #  sql primers old

