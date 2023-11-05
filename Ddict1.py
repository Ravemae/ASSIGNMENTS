'''data = [
    {
        "name": "Mike",
        "place_visited": ("Edo", "Lagos", "Abuja")
    },
    {
        "name": "Jacob"
        "places_visited": ("UK", "US", "China")
    }
]

"""
Write your code between the starting code and the print statement
Instruction:
1. Add a New Dictionary Inside the data list dynamically
2. Add a value to places visited to each dictionary
"""

print(data)'''
Data = [
    (   
        "Mike",
        "Edo", "Lagos", "Abuja"
    ),
    (
        "Jacob",
        "UK", "US", "China"
    )
],

Information = [
    (   
        "Mike" ,
        "Edo", "Lagos", "Abuja"
    ),
    (
        "Jacob" ,
        "UK", "US", "China"
    ),
    (   
        "Vera" ,
        "Dubai", "US", "Paris"
    )
]
Data =Information
t_change = list(Information)
t_change[0] = Information
Data = tuple(t_change)
print(Information)