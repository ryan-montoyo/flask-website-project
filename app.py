from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'title': 'Security Guard, Sanctum Sanctorum',
    'location': 'Hong Kong, China',
    'salary' : '$9,000,000/Year'
  },
  {
    'id' : 2,
    'title': 'Beer Truck Driver',
    'location': 'New Asgard',
  },
  {
    'id' : 3,
    'title': "Peter Parker's Math Tutor",
    'location': 'New York City, USA',
    'salary' : '$19,000/Year'
  },
  {
    'id' : 4,
    'title': 'Janitor, Avengers Tower',
    'location': 'New York City, USA',
    'salary' : '$900,000/Year'
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