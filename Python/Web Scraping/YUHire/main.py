from bs4 import BeautifulSoup
import requests

# Posting Object -- Used as a generalized container for the abstract object
class Posting:
    def __init__(self, faculty: str, campus: str, province: str):
        self.faculty = faculty
        self.campus = campus
        self.province = province

    def summary(self) -> str:
        return "Faculty / Affiliation: {}\nCampus Location: {}\nProvince: {}\n".format(
            self.faculty, self.campus, self.province
        )


print("===== YUHire Tool =====")
# Scraping Parameters
html_text = requests.get("https://jobs-ca.technomedia.com/yorkuniversity/")
soup = BeautifulSoup(html_text.text, "lxml")
jobs = soup.find_all("div", class_="col-sm-3 latestJobItems")
# General Mapping for Filtering Purposes
unique_entries = {}

for job in jobs:
    job_title = job.find("div", class_="col-xs-12 jobName").text.strip()
    if job_title not in unique_entries.keys():
        position = Posting(job.find("div", class_="col-xs-12 jobEntity").text.strip(),
                           job.find("div", class_="col-xs-12 jobCity").text.strip(),
                           job.find("div", class_="col-xs-12 jobCountry").text.strip())
        unique_entries[job_title] = position

print("Please enter a command sequence: ")
print("1) View All Current Featured Jobs")
print("2) View Jobs Based on a Keyword")

try:
    control_sequence = int(input())
    if control_sequence == 1:
        print("The current featured jobs are:\n")
        for item in unique_entries.keys():
            print(item)
            print(unique_entries[item].summary())
    elif control_sequence == 2:
        keyword = input("Keyword:\n").lower()
        for item in unique_entries.keys():
            if keyword in item.lower():
                print(item)
                print(unique_entries[item].summary())
except ValueError:
    print("Incorrect value has been passed to the control sequence.")
finally:
    html_text.close()
    quit(0)
