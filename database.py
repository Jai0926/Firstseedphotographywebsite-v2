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

def add_application_to_db(services_id,data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications(services_id,full_name,email,Shoot_Enquiry,Shoot_Requirement,Phone_Number) VALUES(:services_id, :full_name, :email, :Shoot_Enquiry, :Shoot_Requirement,:Phone_Number)")

    conn.execute(query,
                 services_id=services_id,
                 full_name=data['full name'],
                 email=data['email'],
                 Shoot_Enquiry=data['Shoot Enquiry'],
                 Shoot_Requirement=data['Explain'],
                 Phone_Number=data['Phone Number'])