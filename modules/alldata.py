# alldata.py
# all requests should be cached here.

# get() -> grabs all data.
# getTotalsByDay() -> grabs daily totals for all students.
# getStudentAverages() -> grabs daily average per student

import itertools
import datetime

# Grabs all data from API.
# Currently returns fake data
def get():
  return {
    'Bob': [
      (datetime.date(2013, 2, 1), {
        1: {'A': 2, 'B': 2}, 
        2: {'A': 2, 'B': 2}, 
        3: {'A': 1, 'B': 2},
        4: {'A': 0, 'B': 2},
        5: {'A': 1, 'B': 2},
        }), 
      (datetime.date(2013, 2, 2), {
        1: {'A': 2, 'B': 0}, 
        2: {'A': 1, 'B': 1}, 
        3: {'A': 1, 'B': 0},
        4: {'A': 2, 'B': 0},
        5: {'A': 2, 'B': 2},
        }), 
      (datetime.date(2013, 2, 3), {
        1: {'A': 2, 'B': 2}, 
        2: {'A': 2, 'B': 2}, 
        3: {'A': 0, 'B': 0},
        4: {'A': 0, 'B': 0},
        5: {'A': 1, 'B': 0},
        }), 
      (datetime.date(2013, 2, 4), {
        1: {'A': 2, 'B': 2}, 
        2: {'A': 2, 'B': 2}, 
        3: {'A': 2, 'B': 2},
        4: {'A': 2, 'B': 2},
        5: {'A': 2, 'B': 2},
        })
      ],
    'Caroline': [
      (datetime.date(2013, 2, 1), {
        1: {'A': 1, 'B': 2}, 
        2: {'A': 2, 'B': 1}, 
        3: {'A': 2, 'B': 1},
        4: {'A': 2, 'B': 2},
        5: {'A': 2, 'B': 2},
        }), 
      (datetime.date(2013, 2, 2), {
        1: {'A': 2, 'B': 2}, 
        2: {'A': 2, 'B': 2}, 
        3: {'A': 2, 'B': 2},
        4: {'A': 2, 'B': 2},
        5: {'A': 2, 'B': 2},
        }), 
      (datetime.date(2013, 2, 3), {
        1: {'A': 0, 'B': 2}, 
        2: {'A': 1, 'B': 2}, 
        3: {'A': 0, 'B': 2},
        4: {'A': 0, 'B': 2},
        5: {'A': 0, 'B': 2},
        }), 
      (datetime.date(2013, 2, 4), {
        1: {'A': 2, 'B': 2}, 
        2: {'A': 2, 'B': 1}, 
        3: {'A': 2, 'B': 2},
        4: {'A': 2, 'B': 2},
        5: {'A': 2, 'B': 2},
        })
      ]
  }

# ideally should be handled by API
def getTotalsByDay():
  students = get()
  output = { }

  for student in students:
    days = students[student]
    output[student] = [ ]

    for (day, periods) in days:
      total = 0

      for period in periods:
        categories = periods[period]  
        for key, value in categories.iteritems():
          total += value
      
      output[student].append((day, total))

  return output

# ideally should be handled by API
def getStudentAverages():
  students = getTotalsByDay()
  output = { }

  for key, value in students.iteritems():
    student = key
    days = value
    total = 0
    for (day, day_total) in days:
      total += day_total
    output[student] = float(total) / len(days)
  
  return output
