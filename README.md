Zephyr_Analysis
===============

Identifies interesting features in data for Zephyr (PACE)

## Usage

Call `analyze()` from `analyze.py`. In other words,
```
python analyze.py
```

## API Modules

### alldata.py
Set of functions which fetch data from the API, and cache the results.

```python
get()                 # grabs all data.
getTotalsByDay()      # grabs daily totals for all students.
getStudentAverages()  # grabs daily average per student
```

### log.py
Set of functions which use the API to post to the user-facing log.

```python
# Posts a message to the log.
# @GIVEN students, list of strings
# @GIVEN startday, integer
# @GIVEN endday, integer
# @GIVEN description, string
# @GIVEN priority, boolean
# @GIVEN typeid, integer
post(students, (startday, endday), description, priority, typeid)

# Posts a message about a dip in performance to the log.
# @GIVEN students, list of strings
# @GIVEN startday, integer
# @GIVEN endday, integer
postDip(students, (startday, endday)):
```

## Analysis Modules

### dips.py
Fetches data and makes a post about any student whose performance drops below 20% of their average.