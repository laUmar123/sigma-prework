from datetime import date, datetime

current_date_object = datetime.now()

while True:
  user_date = input("Please enter a date in the past using the format DD-MM-YYYY: ")

  if len(user_date) != 10:
    print("Incorrect date format, it must be DD-MM-YYYY")
    continue

  try:
    day = int(user_date[0:2])
    month = int(user_date[3:5])
    year = int(user_date[6:])
  except ValueError:
    print("The date must be numbers excluding the '-'")
    continue
  
  if not(0 < day < 32):
    print("The day is not valid")
    continue

  if not(0 < month < 13):
    print("The month is not valid")
    continue

  if not(0 < year < current_date_object.year + 1):
    print("The year is not valid")
    continue

  user_date_object = datetime(year, month, day)
  break

difference = current_date_object - user_date_object
print(difference.days // 365)