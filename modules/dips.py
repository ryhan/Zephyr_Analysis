# dips.py

import itertools, datetime
import alldata
import log

# Marks any dips in student behavior
def mark():
  students = alldata.getStudentAverages()
  dailytotals = alldata.getTotalsByDay()

  for key, value in students.iteritems():
    student = key
    average = value
    days = dailytotals[student]

    isDip = lambda (day, total): (total <= average*0.8)
    dipDays = map(lambda (day, total): day, filter(isDip, days))
    dips = groupDays(dipDays)

    for (start, end) in dips:
      log.postDip([student], (start, end))

# Group a sorted list of dates into a list of tuples of ranges
# Example: [3, 4, 7, 8, 9, 14] -> [(3,4), (7, 9), (14, 14)]
def groupDays(days):
  periods = [ ]
  priorDay = datetime.date.min
  for day in days:
    if (len(periods) == 0):
      periods = [(day, day)]
    elif ((day - priorDay).days > 1):
      periods.append((day, day))
    else:
      (start, end) = periods[len(periods) - 1]
      periods[len(periods) -1] = (start, day)
    priorDay = day
  return periods