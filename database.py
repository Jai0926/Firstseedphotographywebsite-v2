from sqlalchemy import create_engine,text
import os

db_connection_string = os.environ['db_connection_str']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

def load_services_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from services"))
    services = []
    for row in result.all():
      services.append(dict(row))
    return services


def load_service_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from services where id = :val"),
      val = id
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])