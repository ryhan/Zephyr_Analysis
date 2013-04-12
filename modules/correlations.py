# correlations.py

import dataobjects
import collections
import itertools
import log

# constants
IMP_CHANGE = .2
IMP_FREQ = 5

def mark():
  data = dataobjects.get_pyobj()
  for student, student_data in data.iteritems():
    mark_student(student, student_data)
  
def mark_student(name, student_data):
  startday = student_data[0][0]
  endday = student_data[-1][0]

  # frequency of certain correlations
  per_correlations = collections.defaultdict(int)
  all_correlations = collections.defaultdict(int)
  for (day, periods) in student_data:
    changes = get_changes(periods) # change: {period : [(behavior, dir)]}
    all_changes = [ ]
    per_changes = [ ]
    for period, changes_list in changes.iteritems():
      for change in changes_list:
        all_changes.append(change)
        per_changes.append((period, change[0], change[1]))
     
    # track freq per-period and overall 
    for correlation in itertools.combinations(per_changes, 2):
      if correlation[0][0] == correlation[1][0]: # only if same period
        period = correlation[0][0]
        change1 = correlation[0][1:]
        change2 = correlation[1][1:]
        per_correlation = (period, change1, change2)
        per_correlations[per_correlation] += 1
    for correlation in itertools.combinations(all_changes, 2):
      all_correlations[correlation] += 1

  # log both per-period and overall correlations
  for (per, change1, change2), freq in per_correlations.iteritems():
    if freq >= IMP_FREQ:
      log.postPerCorrInStudent(name, per, change1, change2, (startday, endday))
  for (change1, change2), freq in all_correlations.iteritems():
    if freq >= IMP_FREQ:
      log.postCorrInStudent(name, change1, change2, (startday, endday))

def get_changes(periods):
  changes = collections.defaultdict(list)

  # averages across each behavior over the day
  averages  = collections.defaultdict(list) 
  for period, behaviors in periods.iteritems():
    for behavior, points in behaviors.iteritems():
      averages[behavior].append(points)
  for behavior, totals in averages.iteritems():
    total = sum(totals)
    total_num = len(totals)
    averages[behavior] = float(total)/float(total_num)

  # find changes
  for period, behaviors in periods.iteritems():
    for behavior, points in behaviors.iteritems():
      changed = is_change(points, averages[behavior])
      if changed > 0:
        changes[period].append((behavior, 1))
      elif changed < 0:
        changes[period].append((behavior, -1))

  return changes

def is_change(points, average):
  if points >= average * (1.0 + IMP_CHANGE): return 1
  elif points <= average * (1.0 - IMP_CHANGE): return -1
  else: return 0
