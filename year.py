year = 2016
if year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
elif year % 400 == 0:
    print("Leap Year")
else:
    print("Normal Year")
