from sqlalchemy import create_engine, text
import os

db_connection_string = 'DB_CONNECTION_STRING'

engine = create_engine(db_connection_string)



def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))

    jobs = []
    # Get column names
    column_names = result.keys()

    for row in result:
        job = {}
        for column_name, value in zip(column_names, row):
            job[column_name] = value
        jobs.append(job)
    return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text('select * from jobs where id = :val'), {'val': id})
        row = result.fetchone()
        if row is None:
            return None
        else:
            column_names = result.keys()
            return dict(zip(column_names, row))
        
def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text('INSERT INTO applications (job_id, first_name, last_name, email, linkedin_url, education, work_experience, resume_url) VALUES(:job_id, :first_name, :last_name, :email, :linkedin_url, :education, :work_experience, :resume_url)')
        conn.execute(query, job_id = job_id, first_name = data['first_name'], last_name = data['last_name'], email = data['email'], linkedin_url = data['linkedin_url'],education = data['education'],work_experience = data['work_experience'], resume_url = data['resume_url'])