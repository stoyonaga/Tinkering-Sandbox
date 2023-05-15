from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

"""
YU-Hire Search Automation 
Last Checked: 2023-05-12
"""

# Avoid Memory Leak (Close Operation Once Completed)
with sync_playwright() as p:
    # (chromium, firefox, or webkit are available browsers)
    print("----- Browser Launched -----")
    browser = p.chromium.launch(headless=True)
    # Page Object (for interaction)
    page = browser.new_page()
    page.goto("https://jobs-ca.technomedia.com/yorkuniversity")
    print ("----- Site Reached -----")
    page.is_visible("#modal-content")
    page.click("#btnCookieRejectALL")
    page.click("#liNEWS_INTERNAL_JOBS")
    page.get_by_title("Affiliation *").nth(1).click()
    page.get_by_text("Summer Student").nth(1).click()
    page.click("#btnSearchbutton2_1")
    print("----- Query Launched -----")
    # We sleep here to account for query update to reach the view (html) via controller (javascript) functions
    time.sleep(3)
    html = page.inner_html("#CTG_JOB_LIST")
    print("----- Retrieving Data -----")
    parser = BeautifulSoup(html, "html.parser")
    rows = parser.find_all("tr")
    print("----- Parsing Data -----")
    for entry in rows:
        try:
            job_id = entry.find("td", {"class": "hidden-xs"}).text.strip()
            posting_date = entry.find("td", {"tabindex" : "0"}).text.strip()
            job_name = entry.find("div", {"class": "styleColLink"}).text.strip()
            job_link = "https://jobs-ca.technomedia.com/yorkuniversity/" + entry.find("a", {"class": "relink"})["href"]
            job_department = entry.find("div", {"class": "styleColAdd1"}).text.strip()
            print("[ID: {}][Date Posted: {}]\nJob Name: {}\nDepartment: {}\n-- Application Link --\n{}\n".format(job_id, posting_date, job_name, job_department, job_link))

        except:
            pass
