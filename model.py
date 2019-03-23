import sqlite3


def init_db():
    conn = sqlite3.connect('form.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM tableform")
    except:
        c.execute("CREATE TABLE tableform(NAME text,EMAIL text,PASSWORD text,ADDRESS text,CITY text,STATE text,ZIP state)")
    conn.commit()
    conn.close()

def get_all_data():
    conn=sqlite3.connect('form.db')
    c=conn.cursor()
    results=c.execute("SELECT * FROM tableform")
    todos=[]
    for item in results:
        todos.append([item[0],item[1],item[2],item[3],item[4],item[5],item[6]])
    return todos

def add_newform(formlist):
    conn=sqlite3.connect('form.db')
    c=conn.cursor()
    c.execute("INSERT INTO tableform VALUES (?,?,?,?,?,?,?)",(formlist[0],formlist[1],formlist[2],formlist[3],formlist[4],formlist[5],formlist[6]))
    conn.commit()
    conn.close()
    return


if __name__=='__main__':
    init_db()
