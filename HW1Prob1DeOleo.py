total_miles = 0
total_gallons = 0

while True:

    gallons = float(input("\nEnter the number of gallons used (any negative number to end): "))
    
    if gallons < 0:
        break
    
    miles = float(input("\nEnter the number of miles driven: "))
    mpg = miles / gallons
    
    print(f'\nThe miles/gallon for this tank was {mpg:.6f}.')
    
    total_miles += miles
    total_gallons += gallons

average_mpg = total_miles / total_gallons
print(f'\nThe overall average miles/gallon for the above tankfuls was {average_mpg:.6f}.\n')