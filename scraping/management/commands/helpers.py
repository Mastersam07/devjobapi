from jobs.models import Job
from bs4 import BeautifulSoup
import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0"
}

def weworkremotey_jobs():
        r = requests.get("https://weworkremotely.com/")
        page = BeautifulSoup(r.text, "html.parser")
        job_section = page.find("section", {"id": "category-2"})
        for job in job_section.find_all("li", {"class": "feature"}):
            try:
                # save in db if job doesnt exist
                if not Job.objects.filter(website = "https://weworkremotely.com" + job.find_all("a")[1]["href"]).exists():
                    Job.objects.create(
                        title = job.find("span", {"class": "title"}).text.strip(),
                        location = job.find("span", {"class": "region company"}).text.strip(),
                        type = job.find_all("span", {"class": "company"})[1].text.strip(),
                        company_name = job.find("span", {"class": "company"}).text.strip(),
                        website = "https://weworkremotely.com" + job.find_all("a")[1]["href"],
                        description = weworkremotely_info("https://weworkremotely.com" + job.find_all("a")[1]["href"])["description"],
                        tags = weworkremotely_info("https://weworkremotely.com" + job.find_all("a")[1]["href"])["tags"],
                    )
                    print('%s added' % (job.find("span", {"class": "title"}).text.strip(),))
                else: 
                    print('%s already exists' % (job.find("span", {"class": "title"}).text.strip(),))
            except:
                pass

def weworkremotely_info(href):
    r = requests.get(href)
    page = BeautifulSoup(r.text, "html.parser")

    role = page.find(
        "div", {"class": "listing-header-container"}).find("h1").text.strip()
    tags = [i.text.strip().lower()
            for i in page.find_all("span", {"class": "listing-tag"})]
    description = page.find(
        "div", {"id": "job-listing-show-container"}).text.strip()
    return {
        "tags": tags,
        "description": description
    }


def remoteok_jobs():
    s = requests.Session()
    s.headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0"
    r = s.get("https://remoteok.io/remote-dev-jobs")
    page = BeautifulSoup(r.text, "html.parser")

    first_index = str(page).find("<thead>")
    second_index = str(page)[first_index + 7:].find("<thead>")
    job_section = BeautifulSoup(
        str(page)[first_index:second_index], "html.parser")
    for job in job_section.find_all("tr", {"class": "job"}):
        try:
            # save in db if job doesnt exist
            job_info = json.loads(str(job.find("script"))[35:-9])
            if not Job.objects.filter(website = "https://remoteok.io" + job["data-url"]).exists():
                Job.objects.create(
                    title = job_info["title"],
                    location = job_info["jobLocation"]["address"]["addressCountry"],
                    type = job_info["employmentType"],
                    company_name = job_info["hiringOrganization"]["name"],
                    website = "https://remoteok.io" + job["data-url"],
                    description = job_info["description"],
                    tags = [i.text.strip().lower() for i in job.find("td", {"class": "tags"}).find_all("h3")],
                )
                print('%s added' % (job_info["title"],))
            else: 
                print('%s already exists' % (job_info["title"],))
        except:
            pass


def employremotely_jobs():
    r = requests.get("https://www.employremotely.com/jobs")
    page = BeautifulSoup(r.text, "html.parser")
    for job in page.find_all("div", {"class": "c-job-card"}):
        try:
            if not Job.objects.filter(website = "https://www.employremotely.com" + job.find("span", {"class": "c-job-card__job-title"}).find("a")["href"]).exists():
                Job.objects.create(
                    title = job.find("span", {"class": "c-job-card__job-title"}).find("a").text.strip(),
                    location = job.find("span", {"class": "c-job-card__location"}).text.strip()[2:],
                    type = job.find("span", {"class": "c-job-card__contract-type"}).text.strip()[2:],
                    company_name = job.find("span", {"class": "c-job-card__company"}).text.strip(),
                    website = "https://www.employremotely.com" + job.find("span", {"class": "c-job-card__job-title"}).find("a")["href"],
                    tags = employremotely_info("https://www.employremotely.com" + job.find("span", {"class": "c-job-card__job-title"}).find("a")["href"])["tags"],
                    deadline = employremotely_info("https://www.employremotely.com" + job.find("span", {"class": "c-job-card__job-title"}).find("a")["href"])["deadline"],
                    description = employremotely_info("https://www.employremotely.com" + job.find("span", {"class": "c-job-card__job-title"}).find("a")["href"])["description"],
                )
                print('%s added' % (job.find("span", {"class": "c-job-card__job-title"}).find("a").text.strip(),))
            else: 
                print('%s already exists' % (job.find("span", {"class": "c-job-card__job-title"}).find("a").text.strip(),))
        except:
            pass

def employremotely_info(href):
    r = requests.get(href)
    page = BeautifulSoup(r.text, "html.parser")

    role = page.find("h1", {"class": "u-c--white"}).text.strip()
    deadline = page.find_all(
        "span", {"class": "job-header__detail"})[-1].text.strip()
    tags = [i.text.strip().lower() for i in page.find("section", {
        "class": "job-information__tags"}).find_all("span", {"class": "c-pill"})]
    description = page.find(
        "section", {"class": "job-information__text-block"}).text.strip()
    return {
        "tags": tags,
        "deadline": deadline[2:],
        "description": description
    }


def remotive_jobs():
    r = requests.get("https://remotive.io/remote-jobs/software-dev")
    page = BeautifulSoup(r.text, "html.parser")
    job_section = page.find("ul", {"class": "job-list"})

    for job in job_section.find_all("li"):
        try:
            if job.find("span", {"class": "job-date--old"}):
                continue
            try:
                location = job.find("span", {"class": "location"}).text.strip()
            except:
                location = ""
            if not Job.objects.filter(website = "https://remotive.io" + job["data-url"]).exists():
                    Job.objects.create(
                        title = job.find("a").text.strip(),
                        location = location,
                        company_name = job.find("div", {"class": "company"}).find("span").text.strip(),
                        website = "https://remotive.io" + job["data-url"],
                        description = remotive_info("https://remotive.io" + job["data-url"])["description"],
                        tags = [i.text.strip().lower() for i in job.find_all("a", {"class": "job-tag"})],
                    )
                    print('%s added' % (job.find("a").text.strip(),))
            else: 
                    print('%s already exists' % (job.find("a").text.strip(),))
        except:
            pass

def remotive_info(href):
    r = requests.get(href)
    page = BeautifulSoup(r.text, "html.parser")

    company = page.find("div", {"class": "content"}).find("h2").text.strip()
    role = page.find("div", {"class": "content"}).find("h1").text.strip()
    tags = [i.text.strip().lower() for i in page.find(
        "div", {"class": "job-tags"}).find_all("a", {"class": "job-tag"})]
    description = page.find("div", {"class": "job-description"}).text.strip()
    return {
        "description": description
    }


def stackoverflow_jobs():
    r = requests.get("https://stackoverflow.com/jobs")
    page = BeautifulSoup(r.text, "html.parser")
    job_section = page.find("div", {"class": "listResults"})

    jobs = []
    for job in job_section.find_all("div", {"class": "-job"}):
        try:
            if not Job.objects.filter(website = "https://stackoverflow.com" + job.find("a", {"class": "s-link"})["href"]).exists():
                Job.objects.create(
                    title = job.find("a", {"class": "s-link"})["title"],
                    location = job.find("span", {"class": "fc-black-500"}).text.strip(),
                    company_name = job.find("h3", {"class": "fc-black-700"}).find("span").text.strip(),
                    website = "https://stackoverflow.com" + job.find("a", {"class": "s-link"})["href"],
                    description = stackoverflow_info("https://stackoverflow.com" + job.find("a", {"class": "s-link"})["href"])["description"],
                    tags = [i.text.strip().lower() for i in job.find_all("a", {"class": "post-tag"})],
                )
                print('%s added' % (job.find("a", {"class": "s-link"})["title"],))
            else: 
                print('%s already exists' % (job.find("a", {"class": "s-link"})["title"],))
        except:
            pass

def stackoverflow_info(href):
    r = requests.get(href)
    page = BeautifulSoup(r.text, "html.parser")

    role = page.find("h1", {"class": "fs-headline1 mb4"}).text.strip()
    company = page.find("a", {"class": "fc-black-700"}).text.strip()
    tags = [i.text.strip().lower() for i in page.find_all("section", {"class": "mb32"})[
        1].find_all("a", {"class": "post-tag no-tag-menu"})]
    description = page.find("div", {"id": "overview-items"}).text.strip()
    return {
        "description": description
    }


def github_jobs():
    job_section = requests.get("https://jobs.github.com/positions.json").json()

    for job in job_section:
        try:
            if not Job.objects.filter(website = job["url"]).exists():
                Job.objects.create(
                    title = job["title"],
                    location = job["location"],
                    type = job["type"],
                    company_name = job["company"],
                    website = job["url"],
                    description = job["description"],
                )
                print('%s added' % (job["title"],))
            else: 
                print('%s already exists' % (job["title"],))
        except:
            pass


def remoteco_jobs():
    r = requests.get("https://remote.co/remote-jobs/developer")
    page = BeautifulSoup(r.text, "html.parser")
    job_section = page.find_all("div", {"class": "card-body p-0"})[1]

    for job in job_section.find_all("a", {"class": "card"}):
        try:
            if not Job.objects.filter(website = "https://remote.co" + job["href"]).exists():
                Job.objects.create(
                    title = job.find("span", {"class": "font-weight-bold larger"}).text.strip(),
                    company_name = job.find("p", {"class": "m-0 text-secondary"}).text.strip().split("\n")[0].strip(),
                    website = "https://remote.co" + job["href"],
                    description = remoteco_info("https://remote.co" + job["href"])["description"],
                    location = remoteco_info("https://remote.co" + job["href"])["location"],
                )
                print('%s added' % (job.find("span", {"class": "font-weight-bold larger"}).text.strip(),))
            else: 
                print('%s already exists' % (job.find("span", {"class": "font-weight-bold larger"}).text.strip(),))
        except:
            pass

def remoteco_info(href):
    r = requests.get(href)
    page = BeautifulSoup(r.text, "html.parser")

    role = page.find("h1", {"class": "font-weight-bold"}).text.strip()
    location = page.find("span", {"class": "location_sm"}).text.strip()
    description = page.find("div", {"class": "job_description"}).text.strip()
    return {
        "location": location,
        "description": description
    }


def pythonorg_jobs():
    r = requests.get("https://www.python.org/jobs/")
    page = BeautifulSoup(r.text, "html.parser")
    job_section = page.find("ol", {"class": "list-recent-jobs"})

    for job in job_section.find_all("li"):
        try:
            if not Job.objects.filter(website = "https://www.python.org" + job.find("span", {"class": "listing-company-name"}).find("a")["href"]).exists():
                Job.objects.create(
                    title = job.find("span", {"class": "listing-company-name"}).find("a").text.strip(),
                    company_name = job.find("span", {"class": "listing-company-name"}).text.strip().split("\n")[-1].strip(),
                    website = "https://www.python.org" + job.find("span", {"class": "listing-company-name"}).find("a")["href"],
                    description = pythonorg_info("https://www.python.org" + job.find("span", {"class": "listing-company-name"}).find("a")["href"])["description"],
                    location = pythonorg_info("https://www.python.org" + job.find("span", {"class": "listing-company-name"}).find("a")["href"])["location"],
                    tags = [i.strip().lower() for i in job.find("span", {"class": "listing-job-type"}).text.split(",")],
                )
                print('%s added' % (job.find("span", {"class": "listing-company-name"}).find("a").text.strip(),))
            else: 
                print('%s already exists' % (job.find("span", {"class": "listing-company-name"}).find("a").text.strip(),))
        except:
            pass

def pythonorg_info(href):
    r = requests.get(href)
    page = BeautifulSoup(r.text, "html.parser")

    description = page.find("div", {"class": "job-description"}).text.strip()
    location = page.find("span", {"class": "listing-location"}).text.strip()
    return {
        "location": location,
        "description": description
    }


def hackerrank_jobs():
    r = requests.get("https://www.hackerrank.com/jobs/search", headers=headers)
    page = BeautifulSoup(r.text, "html.parser")
    job_section = page.find("div", {"class": "jobs-list"})

    jobs = []
    for job in job_section.find_all("a", {"class": "job-card"}):
        try:
            jobs.append({
                "href": "https://www.hackerrank.com" + job["href"],
                "company": job.find("span", {"class": "job-card-company-name"}).text.strip(),
                "role": job.find("h2").text.strip(),
                "location": job.find("li", {"class": "job-card-field"}).text.strip(),
                "experience": job.find_all("li", {"class": "job-card-field"})[1].text.strip()
            })
            if not Job.objects.filter(website = "https://www.hackerrank.com" + job["href"]).exists():
                Job.objects.create(
                    title = job.find("h2").text.strip(),
                    location = job.find("li", {"class": "job-card-field"}).text.strip(),
                    company_name = job.find("span", {"class": "job-card-company-name"}).text.strip(),
                    website = "https://www.hackerrank.com" + job["href"],
                    description = hackerrank_info("https://www.hackerrank.com" + job["href"])["description"],
                )
                print('%s added' % (job.find("h2").text.strip(),))
            else: 
                print('%s already exists' % (job.find("h2").text.strip(),))
        except:
            pass

def hackerrank_info(href):
    r = requests.get(href, headers=headers)
    page = BeautifulSoup(r.text, "html.parser")

    description = page.find(
        "div", {"class": "job-description-v2"}).text.strip()
    return {
        "description": description
    }