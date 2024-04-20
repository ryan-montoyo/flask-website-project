from flask import Flask, render_template, jsonify

from database import load_jobs_from_db

app = Flask(__name__)



@app.route("/")
def hello_avengers():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs = jobs, company_name = 'Avengers')

@app.route('/api/jobs')
def listJobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)