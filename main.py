print("Leap Year check.")
year = int(input("Which year do you want to check?:\n"))

if year%4==0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year.")
        else:
            print(f"The year {year} is NOT a leap year.")
    else:
        print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is NOT a leap year.")
    
#MAYBE SHORTER ALTERNATIVE:
#if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#  print("Leap year.")
#elif year % 4 == 0 and year % 100 != 0:
#  print("Leap year.")
#else:
#  print("Not leap year.")
