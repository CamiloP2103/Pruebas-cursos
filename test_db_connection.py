import pymysql
import sys

# Parámetros de conexión - reemplaza con los datos de tu servidor
HOST = '3.145.105.164'
USER = 'UserPlataforma'
PASSWORD = 'Ucatolica1'
DATABASE = 'plataformacursos'
PORT = 3306  # Puerto por defecto de MySQL

def test_connection():
    try:
        # Intentar establecer conexión
        connection = pymysql.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE,
            port=PORT,
            connect_timeout=5
        )
        
        print("¡Conexión exitosa a la base de datos plataformacursos!")
        
        # Prueba una consulta sencilla
        with connection.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            print(f"Versión del servidor MySQL: {version[0]}")
            
            # Verificar las tablas existentes
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            print("Tablas en la base de datos:")
            for table in tables:
                print(f"- {table[0]}")
            
            # Verificar datos en tblusuarios
            cursor.execute("SELECT COUNT(*) FROM tblusuarios")
            count = cursor.fetchone()[0]
            print(f"Número de usuarios en tblusuarios: {count}")
            
            # Verificar datos en tbltipousuarios
            cursor.execute("SELECT COUNT(*) FROM tbltipousuarios")
            count = cursor.fetchone()[0]
            print(f"Número de tipos de usuario en tbltipousuarios: {count}")
            
            # Mostrar los tipos de usuario
            cursor.execute("SELECT IntTipoUsuario, strNombre FROM tbltipousuarios")
            tipos = cursor.fetchall()
            print("Tipos de usuario configurados:")
            for tipo in tipos:
                print(f"- ID: {tipo[0]}, Nombre: {tipo[1]}")
                
        connection.close()
        return True
        
    except pymysql.MySQLError as e:
        error_code = e.args[0]
        error_message = e.args[1]
        print(f"Error de conexión: {error_code} - {error_message}")
        return False
    except Exception as e:
        print(f"Error inesperado: {e}")
        return False

if __name__ == "__main__":
    print("Probando conexión a la base de datos...")
    result = test_connection()
    sys.exit(0 if result else 1)