from flask import Flask, render_template,jsonify

app = Flask(__name__)

Services =[
  {
    'id': 1,
    'title': 'New Born Photography',
    'location':'Bengaluru ,India',
    'Charges': 'Rs. 5000'
  },
  
  {
    'id': 2,
    'title': 'Maternity Photography',
    'location':'Bengaluru ,India',
    'Charges': 'Rs. 8000'
  },

  {
    'id': 3,
    'title': 'Toddler Photography',
    'location':'Bengaluru ,India',
    'Charges': 'Rs. 10000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         services= Services)

  @app.route("/api/services")
  def list_jobs():
    return jsonify(Services)
    

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)