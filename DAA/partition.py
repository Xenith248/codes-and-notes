

#Modify the partition() function in quicksort to implement the following. Take a list as input This list contains the firstname, lastname and date of birth of n persons. Priorit rule for a person:
###First letter of firstname (ii) First letter of lastname (iii) Date of birth.In case of clash we look for second rule and if there is a clash then look for the third rule. 
#Print the position of the chosen person in the list according to his/her priority.
#Show the best case, worst case and average case time taken for 5 element list
#Example:
#Input Anil Kumar 04/04/2000, Amit Kumar 04/04/2001, Asraf Seikh 08/12/2008
#Position of Asraf Seikh is 3

import pandas as pd

def custom_compare(person1, person2):
    first_name1, last_name1, dob1 = person1
    first_name2, last_name2, dob2 = person2
    
    if first_name1[0] < first_name2[0]:
        return -1
    elif first_name1[0] > first_name2[0]:
        return 1
    else:
        if last_name1[0] < last_name2[0]:
            return -1
        elif last_name1[0] > last_name2[0]:
            return 1
        else:
            dob1_date = pd.to_datetime(dob1)
            dob2_date = pd.to_datetime(dob2)
            if dob1_date.day < dob2_date.day:
                return -1
            elif dob1_date.day > dob2_date.day:
                return 1
            else:
                return 0

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if custom_compare(arr[j], pivot) < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


people = [
    ("Anil", "Kumar", "04/04/2000"),
    ("Amit", "Kumar", "04/04/2001"),
    ("Asraf", "Seikh", "08/12/2008")
]


quicksort(people, 0, len(people) - 1)


chosen_person = ("Asraf", "Seikh", "08/12/2008")
position = people.index(chosen_person) + 1

print(f"Position of {chosen_person[0]} {chosen_person[1]} is {position}")
