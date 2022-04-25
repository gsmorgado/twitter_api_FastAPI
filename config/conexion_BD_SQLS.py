import pyodbc

server = 'DESKTOP-J6KNJR1\MSSQLSERVEREX'
bd = 'platzi'
usuario = 'sa'
contrasena = '123456'

conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+bd+';UID='+usuario+';PWD='+ contrasena)
cursor = conexion.cursor()    
cursor.execute('select * from cliente')   


#Get values
all_values = cursor.fetchall()

cursor.close()
conexion.close()

print('Get values: ', all_values)