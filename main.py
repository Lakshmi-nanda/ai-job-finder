from fetchers.infopark import fetch_jobs as fetch_infopark_jobs
from fetchers.technopark import fetch_jobs as fetch_technopark_jobs
from utils.job_tracker import load_sent_jobs, save_sent_jobs, is_new_job, add_job
from email_sender import send_email

print("Searching Infopark...")
infopark_jobs = fetch_infopark_jobs()

print("Searching Technopark...")
technopark_jobs = fetch_technopark_jobs()

jobs = infopark_jobs + technopark_jobs

print(f"Total jobs fetched: {len(jobs)}")

sent_jobs = load_sent_jobs()

new_jobs = []

for job in jobs:
    if is_new_job(job, sent_jobs):
        new_jobs.append(job)
        add_job(job, sent_jobs)

save_sent_jobs(sent_jobs)

print(f"Found {len(new_jobs)} new job(s).")

if new_jobs:
    send_email(new_jobs)
    print("Email sent successfully!")
else:
    print("No new jobs found. Email not sent.")