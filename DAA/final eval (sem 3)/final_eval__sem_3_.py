'''
QUESTION 1

Modify the partition() function in quicksort to implement the following. Take a list as input.
This list contains the firstname, lastname and date of birth of n persons. Priority rule for a person:
(i)	First letter of firstname 
(ii) First letter of lastname 
(iii) Date of birth. 
In case of clash we look for second rule and if there is a clash then look for the third rule. 
Print the position of the chosen person in the list according to his/her priority. 
Show the best case, worst case and average case time taken for 5 element list.

Example:
Input Anil Kumar 04/04/2000, Amit Kumar 04/04/2001, Asraf Seikh 08/12/2008  
Position of Asraf Seikh is 3



ANSWER 1
'''

#defining the the partition funtion
def partition(list, low, high):
    i = low - 1
    pivot = list[high]

    for j in range(low, high):
        if list[j][0] <= pivot[0]:
            i += 1
            #swap
            list[i], list[j] = list[j], list[i]

    list[i + 1], list[high] = list[high], list[i + 1]
    #returning the next element
    return i + 1 

#Defining the quicksort recursive function
def quicksort(list, low, high):
    if low < high:
        pivot_index = partition(list, low, high)

        quicksort(list, low, pivot_index - 1)
        quicksort(list, pivot_index + 1, high)

#Sorting the people according to the question
def sortPeople(list):
    quicksort(list, 0, len(list) - 1)
    return list

people = [
    ["Bipul", "Bahadur", "1/4/1969"],
    ["Devansh", "Bariya", "23/9/1999"],
    ["Ajay", "Kumar", "2/3/2000"],
    ["Aryan", "kaintura", "27/8/2004"]
    
]

sorted_people = sortPeople(people)
print("The Sorted list is")
for person in sorted_people:
    print(person)


'''
--------------------------------------------------------------
QUESTION 2

Modify Bellman Ford algorithm to find longest path from the given source to the destination via a given node. 
Analyze the time taken for the code written by you.


ANSWER 2
'''

def relax(edge, dist, longest_dist):
    src, dest, weight = edge
    if dist[src] + weight > dist[dest]:
        dist[dest] = dist[src] + weight
        longest_dist[dest] = longest_dist[src] + weight
    elif dist[src] + weight == dist[dest]:
        longest_dist[dest] = max(longest_dist[dest], longest_dist[src] + weight)

def initialize(graph, source, dist, longest_dist):
    for node in graph:
        dist[node] = float('-inf')
        longest_dist[node] = 0
    dist[source] = 0
    longest_dist[source] = 0
  
def longestPath(graph, source, destination, destination_node):
    dist = {node: 0 for node in graph}
    longest_dist = {node: 0 for node in graph}

    dist[source] = 0
    longest_dist[source] = 0

    for _ in range(len(graph) - 1):
        for edge in graph:
            relax(edge, dist, longest_dist)

    longest_path = longest_dist[destination]
    path = [destination]

    while path[-1] != source:
        for edge in graph:
            src, dest, weight = edge
            if dist[src] + weight == dist[dest] and longest_dist[dest] == longest_path:
                path.append(src)
                break

    return longest_path, path[::-1]

#driver code
graph = [
    ('A', 'B', 3),
    ('A', 'C', 5),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1),
    ('D', 'E', 3)
]

source = 'A'
destination = 'E'
destination_node = 'D'

longest_path, path = longestPath(graph, source, destination, destination_node)
print("Longest path length:", longest_path)
print("Path:", path)