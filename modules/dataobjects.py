import json
import os
import csv
import datetime
import datasheet_consts as dconsts

# CONSTANTS
FOLLOW_DIRECTIONS = 'follow_directions'
COMPLETE_WORK = 'complete_work'
KIND_WORDS = 'kind_words'
SAFETY_POINTS = 'safety_points'

"""
String of date in "January 14, 1990" format to a string
in standardized "011490" format.
"""
def make_date(date_string):
  months = {
    "January": "01", 
    "February": "02", 
    "March": "03", 
    "April": "04", 
    "May": "05", 
    "June": "06", 
    "July": "07", 
    "August": "08", 
    "September": "09", 
    "October": "10", 
    "November": "11", 
    "December": "12"
  }

  date_parts = date_string.split(" ")
  year = date_parts[2][2:]
  month = months[date_parts[0]]
  day = date_parts[1][:-1]
  day = str(day) if  (len(day) == 2) else ('0' + str(day))
  return datetime.date(int(year), int(month), int(day))

"""
Returns a list of open csv files
"""
def get_data():
  datafiles = [ ]
  os.chdir("../data")
  for f in os.listdir("."):
    if f.endswith(".csv"):
      datafiles.append(open(f, "rb"))
  return datafiles

"""
Distributes (arbitrarily) day behaviors among given number of periods
Input
  day_behaviors : behavior type -> count
Return
  list[(period_num, dict{behavior type -> count})]
"""
def distribute(day_behaviors, num_periods):
  period_behaviors = { }
  for i in range(num_periods):
    period_behaviors[i+1] = { }
  for behavior, count in day_behaviors.iteritems():
    count_distributed = 0
    for i in range(count):
      period = (i % num_periods) + 1
      if period in period_behaviors and behavior in period_behaviors[period]:
        period_behaviors[period][behavior] += 1
      else: 
        period_behaviors[period][behavior] = 1
  return period_behaviors

"""
Returns:
dict of (name of student ->
  list of (day, 
    list of (period, 
      dict of (behavior -> count))))
"""
def get_pyobj():
  data = { }
  
  for datafile in get_data():
    reader = csv.reader(datafile)
    name = datafile.name.split(".")[0]
    dates = [ ]
    for row in reader:
      if row[3] == '': continue # blank or absent
      if row[0] == 'Notes': continue #headers
  
      date = row[2].split(", ", 1)
      date = make_date(date[1])
  
      day_behaviors = {}
      day_behaviors[FOLLOW_DIRECTIONS] = int(row[dconsts.FOLLOWDIR_INDEX])
      day_behaviors[COMPLETE_WORK] = int(row[dconsts.COMPWORK_INDEX])
      day_behaviors[KIND_WORDS] = int(row[dconsts.KINDWORDS_INDEX])
      day_behaviors[SAFETY_POINTS] = int(row[dconsts.SAFETYPTS_INDEX])
      period_behaviors = distribute(day_behaviors, 10)
  
      dates.append((date, period_behaviors))
    data[name] = dates

  return data

def get_jsonobj():
   return json.dumps(get_pyobj()) 
