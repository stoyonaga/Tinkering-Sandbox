from bs4 import BeautifulSoup
import requests
# import time

"""
- This is my adapted version of code from the web scraping tutorial provided by 
  FreeCodeCamp
  
  Original Video: https://www.youtube.com/watch?v=XVv6mJpFOb0
  
  Improvements:
  1) Ability to search for specific job titles 
  2) Ability to search for specific job areas (cities)
  3) Ability to filter out jobs with unfamiliar skill inputs
  4) Code Readability
  5) Package Installer for Linux // WSL2
"""


def find_jobs() -> None:
    job = input("Job Title: ")
    city = input("What city would you like to work in? ")
    unfamiliar_skill = input("Put some skills that you are not familiar with: (comma separated) \n")
    print("Filtering out {}".format(unfamiliar_skill))
    unfamiliar_skills = set(unfamiliar_skill.lower().strip().replace(" ", "").split(","))

    html_text = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit"
        "&txtKeywords={}&txtLocation={}".format(job, city))
    soup = BeautifulSoup(html_text.text, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    for job in jobs:
        published_date = job.find("span", class_="sim-posted").span.text.strip()
        if "few" in published_date:
            company_name = job.find("h3", class_="joblist-comp-name").text.strip()
            skills = job.find("span", class_="srp-skills").text.strip().replace(" ", "").lower()
            set_skills = set(skills.split(","))
            more_info = job.header.h2.a["href"]
            if len(unfamiliar_skills.intersection(set_skills)) == 0:
                print("Job Title: {}".format(job.header.h2.text.strip()))
                print("Company Name: {}".format(company_name.strip()))
                print("Required Skills: {}".format(skills.strip()))
                print("More Information: {}".format(more_info))
                print()
    html_text.close()


print("========== TimesJobs.com Parser ==========")
print()
find_jobs()
quit(0)


# if __name__ == "__main__":
#     while True:
#         find_jobs()
#         print("Sleeping.....")
#         # Sleep for about 10 minutes
#         time.sleep(600)
