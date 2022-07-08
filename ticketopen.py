import argparse
import sqlite3

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('id')

a = argument_parser.parse_args()

x = ('Open', a.id,)

con = sqlite3.connect('customertickets.db')

cur = con.cursor()

cur.execute('INSERT INTO tickets VALUES (?, ?)', x)
con.commit()

con.close()
