import json
import os
from datetime import date

SENT_JOBS_FILE = "data/sent_jobs.json"


def load_sent_jobs():
    if not os.path.exists(SENT_JOBS_FILE):
        return []

    with open(SENT_JOBS_FILE, "r") as file:
        return json.load(file)


def save_sent_jobs(sent_jobs):
    with open(SENT_JOBS_FILE, "w") as file:
        json.dump(sent_jobs, file, indent=4)


def is_new_job(job, sent_jobs):

    for saved_job in sent_jobs:
        if saved_job["link"] == job.link:
            return False

    return True


def add_job(job, sent_jobs):

    sent_jobs.append(
        {
            "title": job.title,
            "company": job.company,
            "link": job.link,
            "posted_date": job.posted_date,
            "saved_on": str(date.today())
        }
    )