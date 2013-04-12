# log.py

# Human-readable flag messages
DIP_IN_PERFORMANCE_MESSAGE = "There was a 20% drop in performance."
CORRELATION_IN_STUDENT_MESSAGE = "When {0} is {1} at {2}, he/she is {3} at {4}."
PER_CORRELATION_IN_STUDENT_MESSAGE = "During period {0}, when {1} is {2} at {3}, he/she is {4} at {5}."

# Posts messages to the Zephyr log via API.
# students -> list of strings
# startday -> integer
# endday -> integer
# description -> string
# priority -> boolean
# typeid -> integer
def post(students, (startday, endday), description, priority, typeid):
  # posts to server.
  print("Post ranging from day " + str(startday) + " to " + str(endday))
  print("Students: " + " and ".join(students))
  print("Issue: " + description + "\n")

def postDip(students, (startday, endday)):
  post(students, (startday, endday), DIP_IN_PERFORMANCE_MESSAGE, True, '1')

def postCorrInStudent(name, change1, change2, (startday, endday)):
  (bhvr1, dir1) = change1
  (bhvr2, dir2) = change2
  get_direction = lambda x: "better" if x > 0 else "worse"
  dir1 = get_direction(dir1)
  dir2 = get_direction(dir2)
  post([name], (startday, endday), 
    CORRELATION_IN_STUDENT_MESSAGE.format(name, dir1, bhvr1, dir2, bhvr2),
    False, '2')

def postPerCorrInStudent(name, per, change1, change2, (startday, endday)):
  (bhvr1, dir1) = change1
  (bhvr2, dir2) = change2
  get_direction = lambda x: "better" if x > 0 else "worse"
  dir1 = get_direction(dir1)
  dir2 = get_direction(dir2)
  post([name], (startday, endday), 
    PER_CORRELATION_IN_STUDENT_MESSAGE.format(per, name, dir1, bhvr1, dir2, bhvr2),
    False, '2')
 
