import psycopg2


conn = psycopg2.connect(
    host="ec2-54-211-160-34.compute-1.amazonaws.com",
    database="damuv96ke368nv",
    user="hkbbigjjpulghz",
    password="10b9630769d732718011d7a679ee3e8cc695b0f0289a1c4bd0e198bb4e0efae6")




def catalogo():
    
    cursor = conn.cursor()
    query="SELECT * FROM productos"
    
    
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        if data:
            return data
        else:
            print("no encontro")
            return False
    except Exception as e:
        print(e)
        return e
    cursor.close() 
    conn.close()
