from fetchers.infopark import fetch_jobs
from utils.job_tracker import (
    load_sent_jobs,
    save_sent_jobs,
    is_new_job,
    add_job
)
from email_sender import send_email

print("\nSearching Infopark...\n")

jobs = fetch_jobs()

sent_jobs = load_sent_jobs()

new_jobs = []

for job in jobs:

    if is_new_job(job, sent_jobs):
        new_jobs.append(job)
        add_job(job, sent_jobs)

save_sent_jobs(sent_jobs)

print(f"\nFound {len(new_jobs)} new job(s)\n")

if new_jobs:

    for job in new_jobs:

        print("=" * 60)
        print(f"Title       : {job.title}")
        print(f"Company     : {job.company}")
        print(f"Posted Date : {job.posted_date}")
        print(f"Location    : {job.location}")
        print(f"Source      : {job.source}")
        print(f"Link        : {job.link}")

    print("\nSending email...\n")
    send_email(new_jobs)

else:
    print("No new jobs found. Email not sent.")