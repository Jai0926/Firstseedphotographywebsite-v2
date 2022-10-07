from sqlalchemy import create_engine,text
import os

db_connection_string = os.environ['db_connection_str']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

def services_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from services"))
    services = []
    for row in result.all():
      services.append(dict(row))
    return services
