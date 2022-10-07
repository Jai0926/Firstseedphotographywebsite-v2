from sqlalchemy import create_engine,text

db_connection_string = "mysql+pymysql://wiinpk8tjw52kd7ft470:pscale_pw_3m8gIgP7io4SQHzxv7TlX707xvGfekQnoHrnlc2Zyfi@us-east.connect.psdb.cloud/first_seed09?charset=utf8mb4"

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
