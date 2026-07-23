import requests
from bs4 import BeautifulSoup

from fetchers.base import Job
from utils.filter import is_matching_job


def fetch_jobs():

    url = "https://infopark.in/companies-job?search=business+analyst"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    tables = soup.find_all("table")

    if not tables:
        return []

    jobs = []

    rows = tables[0].find_all("tr")

    for row in rows:

        columns = row.find_all("td")

        if len(columns) < 5:
            continue

        posted_date = columns[0].get_text(strip=True)
        title = columns[1].get_text(strip=True)

        if not is_matching_job(title):
            continue
            
        company = columns[2].get_text(strip=True)

        details = columns[4].find("a")

        link = ""

        if details:
            link = details.get("href")

        jobs.append(
            Job(
                title=title,
                company=company,
                location="Infopark",
                experience="Not Available",
                link=link,
                source="Infopark",
                posted_date=posted_date,
            )
        )

    return jobs