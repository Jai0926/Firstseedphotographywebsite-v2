from flask import Flask, render_template,jsonify
from database import services_db


app = Flask(__name__)

@app.route("/")
def hello_world():
  services = services_db()
  return render_template('home.html',
                         services=services)

  @app.route("/api/services")
  def list_jobs():
    return jsonify(services)
    

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)