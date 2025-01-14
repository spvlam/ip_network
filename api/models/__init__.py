from contextvars import ContextVar
from peewee import Model
from playhouse.postgres_ext import PostgresqlExtDatabase
import os
from dotenv import load_dotenv
db_context_var: ContextVar[PostgresqlExtDatabase] = ContextVar("db")

load_dotenv()
db_name = os.getenv("DB_NAME") 
db_user = os.getenv("DB_USER")
db_host =os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_pass = os.getenv("DB_PASSWORD")

psql_db = PostgresqlExtDatabase(
    db_name,
    user=db_user,
    password=db_pass,
    host=db_host,
    port=db_port,
    # auto rollback if some thing wrong in database transaction
    autorollback=True,
)

def create_db():
    """Create db connection"""
    return psql_db

def _get_db():
    if db_context_var.get(None) is None:
        db_context_var.set(create_db())
    return db_context_var.get()


class _DBProxy:
    def __getattr__(self, item):
        return getattr(_get_db(), item)

    def __setattr__(self, key, value):
        return setattr(_get_db(), key, value)

db = _DBProxy()


class PeeweeBaseModel(Model):
    class Meta:
        database = psql_db
        schema = "public"
        legacy_label_names = False

if __name__ == '__main__':
    try:
        db.connect()
        print("connect to db successfully")
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        if not db.is_closed():
            db.close()