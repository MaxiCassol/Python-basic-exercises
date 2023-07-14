import sqlite3

db_connection = sqlite3.connect('mydb.db')

db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")
db_cursor.execute("INSERT INTO Alumnos VALUES(1,'maxi', 'cassol')")
db_cursor.execute("INSERT INTO Alumnos VALUES(2,'natalia', 'silva')")
db_cursor.execute("INSERT INTO Alumnos VALUES(3,'amelia', 'cassol')")
db_cursor.execute("INSERT INTO Alumnos VALUES(4,'mina', 'cassol')")
db_cursor.execute("INSERT INTO Alumnos VALUES(5,'lola', 'silva')")
db_cursor.execute("INSERT INTO Alumnos VALUES(6,'charly', 'cassol')")
db_cursor.execute("INSERT INTO Alumnos VALUES(7,'pezUno', 'noSeSabe')")
db_cursor.execute("INSERT INTO Alumnos VALUES(8,'pezDos', 'noSeSabe')")

db_connection.commit()
db_cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'natalia'")

busqueda = db_cursor.fetchall()

print(busqueda)

db_connection.close()