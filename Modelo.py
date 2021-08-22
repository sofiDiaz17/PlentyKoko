import pyodbc 


#conn = pyodbc.connect('Driver={SQL Server};'
 #                     'Server=RON\SQLEXPRESS;'
  #                    'Database=TestDB;'
   #                   'Trusted_Connection=yes;')


conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-GRETRIB;DATABASE=TAREA2;Trusted_Connection=yes')

#cursor = conn.cursor()
#cursor.execute('SELECT * FROM TAREA2.dbo.DimCliente')
#rows = cursor.fetchall()
#for row in rows:
    #print(row)


def catalogo():
    
    cursor = conn.cursor()
    query="SELECT * FROM PlentyKoko.dbo.Productos"
    
    
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        if data:
            return data
        else:
            return False
    except Exception as e:
        return e
    cursor.close() 
    conn.close()