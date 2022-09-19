# TimeCalculator
A project that was provided by freeCodeCamp. The program takes two time values and calculates the time that has elapsed and provides the results. Conditions of the program can be found below or in the link with more details: https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

Write a function named add_time that takes in two required parmeters and one optional parameter:
- a start time in the 12-hour clock format (ending in AM or PM)
- a duration time that indicates the number of hours and minutes
- (optional) a starting day of the week, case insensitive

The function should add the duration time to the start time and return the result. If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.


Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

# Development
Write your code in time_calculator.py. For development, you can use main.py to test your time_calculator() function. Click the "run" button and main.py will run.

# Testing
The unit tests for this project are in test_module.py. We imported the tests from test_module.py to main.py for your convenience. The tests will run automatically whenever you hit the "run" button.
