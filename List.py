#Where user can add filament names in the list
thislist = []
thislist.append(input("Enter filament name: "))
print(thislist)

#For when the user wants to see all the filament stored in the list
if input("Do you want to see a copy of the list? (y/n): ") == "y":
    print(thislist.copy())
else:
    print("No filament requested.")