
SQLITE = "sqlite:///project.db"
POSTGRESQL = "postgresql+psycopg2://postgres:Ordo_400@localhost:5432/blog_db"

class Config:
    DEBUG = True
    SECRET_KEY ='dev'
     # Configura la conexión a PostgreSQL
    SQLALCHEMY_DATABASE_URI = POSTGRESQL