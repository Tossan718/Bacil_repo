def greet (person, first_time=False) :
    if first_time:
        return "First time for everything, right?" + person
    return "Hello, " + person

def greet_all(people):
    for person in people:  
        print (greet(person))

friends = ["Bob", "Josh", "Kiddos"]

greet_all(friends)