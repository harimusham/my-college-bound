from flask import Flask ,render_template,jsonify
app=Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'froent-end engineer',
    'location':'hyderabad',
    'salary':120000
  },
  {
    'id':2,
    'title':'backend developer',
    'location':'benguluru',
    'salary':900000
  },
  {
   'id':3,
    'title':'java developer',
    'location':'kattangur',
    'salary':904533
  },
  {
   'id':4,
    'title':'html developer',
    'location':'nakrekal',
    'salary':999999
  }
  
]
@app.route("/")
def hello_harikiran():
  return render_template('home.html',jobs=JOBS,company_name="harikiran company")
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)