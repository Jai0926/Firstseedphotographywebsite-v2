from flask import Flask, render_template,jsonify,request
from database import load_services_db,load_service_db,add_application_to_db


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

@app.route("/service/<id>/apply", methods=['post'])
def apply_to_service(id):
   data = request.form
   service= load_service_db(id)
   add_application_to_db(id,data)
   return render_template('application_submited.html',
                         application = data,
                        service=service)
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)