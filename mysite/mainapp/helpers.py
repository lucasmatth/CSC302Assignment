import sqlite3



def make_query(statement):
    con = sqlite3.connect("../../videodata.db")
    con.row_factory = lambda cursor, row: row[0]
    cur = con.cursor()
    return cur.execute(statement).fetchall()

def make_plot(data):
    #this function will take in some data and make a plot out of it somehow
    pass
