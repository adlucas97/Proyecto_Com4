import psycopg2


connection = psycopg2.connect(host = 'localhost', database = 'Vacunados', user = 'postgres', password = 'Adrian3345@')

print("conexion exitosa")

cursor = connection.cursor()

# cursor.execute("DROP TABLE IF EXISTS VACUNADOS")

# sql = """CREATE TABLE VACUNADOS(
#     DPI CHAR(100) PRIMARY KEY,
#     NOMBRE CHAR(100) NOT NULL,
#     PRIMER_APELLIDO CHAR(100) NOT NULL,
#     SEGUNDO_APELLIDO CHAR(100),
#     EDAD INT
# ) """
# cursor.execute(sql)
DPI = 3001709470101
Nombre = 'Adrian'
apellido1 = 'Lucas'
apellido2 = 'Guamuche'
edad = 24
insertar = "insert into public.VACUNADOS(Dpi,Nombre, Primer_apellido, segundo_apellido, edad) values(%s,%s,%s,%s,%s)"
parametros = (str(DPI),Nombre, apellido1, apellido2, str(edad))
cursor.execute(insertar, parametros)
connection.commit()
