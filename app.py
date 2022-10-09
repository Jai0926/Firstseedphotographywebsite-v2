from flask import Flask, render_template,jsonify
from database import load_services_db,load_service_db


app = Flask(__name__)

@app.route("/")
def hello_world():
  services = load_services_db()
  return render_template('home.html',
                         services=services)

  @app.route("/api/services")
  def list_jobs():
    return jsonify(services)

@app.route("/service/<id>")
def show_service(id):
  service = load_service_db(id)
  if not service:
    return "Not Found", 404
  return render_template('servicepage.html',
                         service=service)
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)