import argparse
import builtins
import sqlite3

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('id')

a = argument_parser.parse_args()

x = (a.id,)

con = sqlite3.connect('customertickets.db')

cur = con.cursor()

cur.execute('SELECT status FROM tickets WHERE id = ?', x)
x = cur.fetchone()

con.close()

if x is not None:
    builtins.print(*x)
else:
    builtins.print('free')
