import sqlite3
conn = sqlite3.connect('manageaccountsdb')
curs = conn.cursor()
# curs.execute('drop table credit')
# curs.execute('delete from accounts')
curs.execute('select * from credit')
# curs.execute('create table debit (debit_id integer primary key Autoincrement , name char(50) , amount integer(15) default 0, comments char(100), Date date, constraint ct foreign key(name) references accounts on delete cascade)')
print(curs.fetchall())
conn.commit()	