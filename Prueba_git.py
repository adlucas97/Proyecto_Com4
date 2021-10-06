import psycopg2

modelo = int(input("Ingrese el modelo del vehículo: "))
recorrido = int(input("Ingrese el kilometraje recorrido del vehículo: "))

if ((modelo<2007) and (recorrido>20)):
    print("El vehículo debe renovarse")
    s="Renovación"
elif (((modelo>=2007) and (modelo<=2013)) and (recorrido == 20000)):
    print("El vehículo debe recibir mantenimiento")
    s="Matenimiento"
elif ((modelo>2013) and (recorrido<10000)):
    print("El vehículo está en óptimas condiciones")
    s="Optimo"
else:
    print("Mecánico")
    s = "Mecánico"

#Establecemos la conexión a la base de datos
conexion = psycopg2.connect(host = 'localhost', database="Proyecto_com4",user="postgres", password="Adrian3345@")
#Los parametros son nombre de base, el usuario y la contraseña.
cursor = conexion.cursor() #Asignamos el valor de cursor
#Se debe colocar el nombre de la base de datos antes de la tabla
insertar = "insert into public.Vacunados (modelo, recorrido, estado) values (%s, %s, %s);"
parametros = (str(modelo), str(recorrido), s)
cursor.execute(insertar, parametros)
conexion.commit() 
cursor.execute("select * from taxi")
visualizacion = cursor.fetchall()
for row in visualizacion:
    print("Modelo = ", row[0])
    print("Recorrido = ", row[1])
    print("Estado = ", row[2])
