print("Please enter number of days traveled:")
days_traveled = int(input())

full_weeks = days_traveled//7
remaining_days = days_traveled%7

print(days_traveled, "days are", full_weeks, "weeks and", remaining_days, "days")