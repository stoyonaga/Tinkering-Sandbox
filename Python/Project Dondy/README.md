# Installation

After you clone this repository and cd into Project Dondy, run the following command in the terminal:
```bash
sh install.sh
```

Once the dependencies have been installed, you must import your timetable into courses.txt. Please follow the steps notated below:
1. Entries into the text file must use 24-hour time. 
2. Entries must adhere to the following standard: **DAY-COURSE_CODE-START_TIME-END_TIME-ZOOM_LINK**

To understand the **day** field, please refer to the following table of references:

<table>
  <tr><th>Weekday</th><th>Identifier</th></tr>
  <tr><td>Monday</td><td>0</td></tr>
  <tr><td>Tuesday</td><td>1</td></tr>
  <tr><td>Wednesday</td><td>2</td></tr>
  <tr><td>Thursday</td><td>3</td></tr>
  <tr><td>Friday</td><td>4</td></tr>
  <tr><td>Saturday</td><td>5</td></tr>
  <tr><td>Sunday</td><td>6</td></tr>
</table>

# Software Environments
This script has been developed and tested to run under the following constraints
- Python 3.9.13

