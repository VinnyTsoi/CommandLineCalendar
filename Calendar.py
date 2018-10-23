"""A basic calendar that the user will be able to interact with from the command line"""
#imports
from time import sleep, strftime, gmtime
#username
FIRST_NAME = 'Vman'
#calendar data structure
calendar = {}
#welcome message
def welcome():
  print("Welcome " + FIRST_NAME)
  print("Opening calendar")
  sleep(1)
  #print date
  print(strftime("%A, %B %d, %Y"))
  #print time
  print(strftime("%H:%M:%S", gmtime()))
  sleep(1)

  
def start_calendar():
  welcome()
  start = True
  #user options
  while start:
    print
    print('A to Add')
    print('U to Update')
    print('V to View')
    print('D to Delete')
    print('X to Exit')
    print
    user_choice = raw_input("What would you like to do? ")
    user_choice = user_choice.upper()
    #user choice v for view
    if user_choice == 'V':
      if len(calendar.keys()) == 0:
        print
        print("Calendar empty")
      else:
        for i in calendar:
          print(i + ': '+ calendar[i])
    #update calendar
    elif user_choice == 'U':
      date = raw_input("What date (MM/DD/YYYY): ")
      update = raw_input('Enter the update: ')
      calendar[date] = updateuu
      print
      print('Update successful')
      print
      for i in calendar:
        print(i + ': '+ calendar[i])
    #add to calendar
    elif user_choice == 'A':
      print
      event = raw_input('Enter event: ')
      print
      date = raw_input("Enter date (MM/DD/YYYY): ")
      #validate date
      if len(date) > 10 or len(date) < 10 or int(date[6:]) < int(strftime("%Y")):
        print
        print('An invalid date was entered: ')
        print
        #if invalid date entered
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False
      #add event
      else:
        calendar[date] = event
        print
        print('The event was successfully added')
        print
        for i in calendar:
          print(i + ": " + calendar[i])
    elif user_choice == 'D':
      if len(calendar.keys()) == 0:
        print
        print("Calendar empty")
        print
      else:
        event = raw_input("What event? ")
        #search the calendar
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print
            print('Event deleted')
            print
            for i in calendar:
              print(i + ': ' + calendar[i])
          else:
            print
            print('Incorrect event specified')
            print
    elif user_choice == 'X':
      print
      print("Good bye")
      print
      start = False
    else:
      print
      print('Invalid command entered')
      print
      #start = False
        
#Run app
start_calendar()









