def add_time(start, duration, day = None):

  dayCounter = 0
  weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  count = 0 
  
  #collects the initial hour, minutes, and AM/PM of the start time
  stime = start.split(' ')
  minute = int(stime[0].split(':')[1])
  speriod = stime[1]
  hour = int(start.split(':')[0])

  #switches hour time to 24-hour value (e.g. 3pm = 15pm)
  if hour < 12 and speriod == 'PM':
    hour = hour + 12

  #collects the hours and minutes based on duration time
  uhour = int(duration.split(':')[0])
  uminute = int(duration.split(':')[1])
  
  #calcuates the new time based on start time and duration time
  newHour = hour + uhour
  newMinute = minute + uminute

  #converts minutes over 60 into hour
  if newMinute > 60:
    newMinute = newMinute - 60
    newHour = newHour + 1

  #count how many days has passed by 
  dayCounter = int(newHour / 24)
  if dayCounter > 7:
    count = (dayCounter % 7)
  else:
    count = dayCounter

  #Adjust hour value into 24-hour clock
  while newHour > 24:
    newHour = newHour - 24
    if newHour == 0:
      newHour = newHour + 24

  #Based on 24-hour clock, switches hour value to 12-hour clock and switch to correct AM/PM appropriately 
  if 12 < newHour < 24:
    speriod = 'PM'
    newHour = newHour - 12
  elif 0 < newHour < 12:
    speriod = 'AM'
  elif newHour == 12 and speriod == 'PM':
    speriod = 'AM'
  elif newHour == 12 and speriod == 'AM':
    speriod = 'PM'
  elif newHour == 24 and speriod == 'PM':
    speriod = 'AM'
    newHour = newHour - 12
  elif newHour == 24 and speriod == 'AM':
    speriod = 'PM'
    newHour = newHour - 12

  #Capitalizes the day of the week input
  if day != None:
    day = day.capitalize()
  #Switches to the new day based on how many days have passed
    index = weekdays.index(day)
    count = count + index
    if count == 7:
      count = count % 7 
    day = weekdays[count]
    
  #Formats hour, minute, and AM/PM output
  new_time = str(newHour) + ":" + f"{newMinute:02}" + " " + speriod

  #Prints the day of the week if day hasn't changed
  if day != None:
    new_time = new_time + ", " + day

  #Prints the day of the week if day has changed
  if dayCounter == 1:
    new_time = new_time + " (next day)"
  elif dayCounter > 1:
    new_time = new_time + " (" + str(dayCounter) + " days later)"
    
  return new_time
