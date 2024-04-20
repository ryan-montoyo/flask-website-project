from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title': 'Data Analytst',
    'location': 'Tokyo, Japan',
    'salary' : '$9,000,000'
  },
  {
    'id' : 2,
    'title': 'Software Engineer',
    'location': 'New York City, USA',
  },
  {
    'id' : 3,
    'title': 'Middle School Teacher',
    'location': 'New York City, USA',
    'salary' : '$19,000'
  },
  {
    'id' : 4,
    'title': 'Retail Associate',
    'location': 'Memphis, USA',
    'salary' : '$900,000'
  }

]

@app.route("/")
def helloWorld():
  return render_template('home.html', jobs = JOBS, company_name = 'Avengers')

@app.route('/api/jobs')
def listJobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)