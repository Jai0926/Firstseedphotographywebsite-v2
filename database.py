from sqlalchemy import create_engine,  text

db_connection_string= "mysql+pymysql://wiinpk8tjw52kd7ft470:pscale_pw_3m8gIgP7io4SQHzxv7TlX707xvGfekQnoHrnlc2Zyfi@us-east.connect.psdb.cloud/first_seed09?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"}
    })
  
  
with engine.connect() as conn:
  result = conn.execute(text("select * from services"))
  print("type(result):", type(result))
  result_all = result.all
  print("type(result_all()):", type(result_all))
  print("result_all():", result_all)

