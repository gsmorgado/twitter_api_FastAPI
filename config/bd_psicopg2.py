import traceback
import psycopg2

#Gobal constant

PSQL_HOST= "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "123456"
PSQL_BD = "twitter"

#Connection
try: 
    connection_adress ="""host= %s port =%s user=%s password=%s dbname=%s""" % (PSQL_HOST,PSQL_PORT,PSQL_USER,PSQL_PASS,PSQL_BD)
    conecction = psycopg2.connect(connection_adress)
except Exception:
    traceback.print_exc()

    

"""
cursor = conecction.cursor()

#Query
SQL = "Select * from users"
cursor.execute(SQL)

#Get values
all_values = cursor.fetchall()

cursor.close()
conecction.close()

print('Get values: ', all_values)


     for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Join Date = ", row[2])
            print("Salary  = ", row[3], "\n")



"""