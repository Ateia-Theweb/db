import argparse
import sqlite3

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('id')

a = argument_parser.parse_args()

x = ('Closed', a.id,)

con = sqlite3.connect('customertickets.db')

cur = con.cursor()

cur.execute('UPDATE tickets SET status = ? WHERE id = ?', x)
con.commit()

con.close()
