import requests

from fetchers.base import Job
from utils.filter import is_matching_job


def fetch_jobs():

    jobs = []
    page = 1

    while True:

        url = f"https://technopark.in/api/paginated-jobs?page={page}&search=&type="

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        for item in data["data"]:

            title = item.get("job_title", "").strip()

            if not is_matching_job(title):
                continue

            company = item.get("company", {}).get("company", "").strip()

            posted_date = item.get("posted_date", "")

            job_id = str(item.get("job_listing_id", ""))

            link = f"https://technopark.in/job-details/{job_id}"

            jobs.append(
                Job(
                    title=title,
                    company=company,
                    location="Technopark",
                    experience="",
                    link=link,
                    source="Technopark",
                    posted_date=posted_date,
                )
            )

        if data["next_page_url"] is None:
            break

        page += 1

    return jobs