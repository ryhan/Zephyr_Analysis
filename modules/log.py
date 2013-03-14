# log.py

# Human-readable flag messages
DIP_IN_PERFORMANCE_MESSAGE = "There was a 20% drop in performance."

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