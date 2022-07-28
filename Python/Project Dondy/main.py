import webbrowser as wb
import schedule
import time
import pyautogui as py
import datetime


# Courses Class
class Course:
    def __init__(self, date: int, name: str, start: str, end: str, link: str):
        self.date = date
        self.name = name
        self.start = start
        self.end = end
        self.link = link

    def information(self) -> None:
        print("Course Name: " + self.name)
        print("Start Time: " + self.start)
        print("End Time: " + self.end)


# Read courses from courses.txt and return a list of Course objects
def read_courses() -> list:
    courses = list()
    timetable = open("courses.txt", "r")
    for line in timetable.readlines():
        cache = line.split("-")
        courses.append(Course(int(cache[0]), cache[1], cache[2], cache[3], cache[4]))
    timetable.close()
    return courses


# Print summary of daily courses into the terminal
def get_daily_schedule() -> None:
    courses = read_courses()
    for item in courses:
        if datetime.datetime.today().weekday() == item.date:
            item.information()


# Perform Browser, Mouse, Keyboard, and _____ actions
def schedule_meeting(url: str):
    wb.open(url)
    print("LOG: Browser has been opened\nSleeping for 5 seconds...")
    time.sleep(2)
    print("LOG: Activating Automation (1/2) for Zoom Room Entrance")
    py.press("left")
    time.sleep(2)
    print("LOG: Activating Automation (2/2) for Zoom Room Entrance\n")
    py.press("enter")
    time.sleep(3.5)
    # Depending on your Zoom preferences, the proceeding steps here may need some modification
    py.press("enter")
    print("LOG: Activating Entering Zoom Room...")


# Program will begin to run here..
print("========== Zoom Scheduler Version 1.0.0 ==========")
print("Scheduled Courses for the Day: \n")
get_daily_schedule()

tasks = read_courses()

for course in tasks:
    if course.date == 0:
        schedule.every().monday.at(course.start).do(schedule_meeting, course.link)
    elif course.date == 1:
        schedule.every().tuesday.at(course.start).do(schedule_meeting, course.link)
    elif course.date == 2:
        schedule.every().wednesday.at(course.start).do(schedule_meeting, course.link)
    elif course.date == 3:
        schedule.every().thursday.at(course.start).do(schedule_meeting, course.link)
    elif course.date == 4:
        schedule.every().friday.at(course.start).do(schedule_meeting, course.link)

# Busy Polling
while True:
    schedule.run_pending()
    time.sleep(1)
