from dataclasses import dataclass


@dataclass
class Job:
    title: str
    company: str
    location: str
    experience: str
    link: str
    source: str
    posted_date: str = ""
