import psycopg2

try:
    conn = psycopg2.connect(
        dbname="blog_db",
        user="postgress",
        password="Ordo_400",
        host="localhost",
        port="5432"
    )
    print("Conexión exitosa")
except Exception as e:
    print(f"Error de conexión: {e}")