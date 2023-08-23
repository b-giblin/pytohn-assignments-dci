# Author: Brian Giblin
# Date: 8/23/23
# Description: Takes an input as a float from the user and determines if they have a fever

temperatureInF = float(input("What is your tempurature in \N{DEGREE SIGN}F?:  "))


def check_temp():
  if temperatureInF >= 100.4:
      print(f"You have a fever of {temperatureInF}\N{DEGREE SIGN}F")
  elif temperatureInF >= 99.2 and temperatureInF < 100.4:
      print(f"You have a mild fever of {temperatureInF}\N{DEGREE SIGN}F")
  else:
      print("You are fine.")

check_temp()
