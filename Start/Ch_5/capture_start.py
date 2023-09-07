# Example file for Advanced Python: Language Features by Joe Marini
# Capture pattern matching for assigning values within the match

name = input("What is your name? ")

match name:
    case "":
        print("Hello, anonymous!")
    case "Joe" | "Joseph" as s:
        print(f"Hi there {s}")
    case name:
        print(f"Hello, {name}")
