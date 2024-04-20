from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ.get('DB_CONNECTION_STRING')

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
