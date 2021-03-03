##Create a database and table then do the following by taking the input from keyboard

##1) Insert records
#2) Update records
#3) Delete records


db_host = 'localhost'
db_name = 'sampledb'
db_user = 'postgres'
db_password = 'Veera1234@'

import psycopg2
conn = psycopg2.connect(dbname = db_name,user = db_user,password = db_password,host = db_host)
cur = conn.cursor()
#cur.execute("Create table sam_student(id int Primary key, name varchar);")
#cur.execute("insert into sam_student values (3,'Veera');")
#cur.execute("delete from sam_student where id = 4;")
cur.execute("select * from sam_student;")


for i in cur:
    print(i['name'])

#print(cur.fetchall())
#print(cur.fetchone())
conn.commit()

cur.close()
conn.close()
