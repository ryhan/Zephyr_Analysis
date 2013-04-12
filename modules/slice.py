# slice.py
"""
slices student data according to 
  - period
  - day of week
"""

import dataobjects

MONDAY = "Monday"
TUESDAY = "Tuesday"
WEDNESDAY = "Wednesday"
THURSDAY = "Thursday"
FRIDAY = "Friday"
SATURDAY = "Saturday"
SUNDAY = "Sunday"
WEEKDAYS = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, WEDNESDAY, THURSDAY, 
    FRIDAY, SATURDAY, SUNDAY]

# returns dict{student -> dict{day of week -> dict{behavior ->(freq, total)}}}
def get_by_dow():
  students_by_dow = { }
  student_data = dataobjects.get_pyobj()
  for student in student_data:
    by_dow = { }
    for (date, periods) in student_data[student]:
      weekday = WEEKDAYS[date.weekday()] # indices correspond to day
      if weekday not in by_dow:
        by_dow[weekday] = { }
      for (period, behaviors) in periods.iteritems():
        for (behavior, freq) in behaviors.iteritems():
          if behavior in by_dow[weekday]:
            (prev_freq, total) = by_dow[weekday][behavior]
            by_dow[weekday][behavior] = (freq + prev_freq, total + 2)
          else:
            by_dow[weekday][behavior] = (freq, 2)
    students_by_dow[student] = by_dow
  return students_by_dow

# returns dict{student -> dict{period -> dict{behavior ->(freq, total)}}}
def get_by_per():
  students_by_per = { }
  student_data = dataobjects.get_pyobj()
  for student in student_data:
    by_per = { }
    for (date, periods) in student_data[student]:
      for (period, behaviors) in periods.iteritems():
        for (behavior, freq) in behaviors.iteritems():
          if period not in by_per:
            by_per[period] = { }
          if behavior not in by_per[period]:
            by_per[period][behavior] = (freq, 2)
          else:
            (prev_freq, total) = by_per[period][behavior]
            by_per[period][behavior] = (prev_freq + freq, total + 2)
    students_by_per[student] = by_per
  return students_by_per
