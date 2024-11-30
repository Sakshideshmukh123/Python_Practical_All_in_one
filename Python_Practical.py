print("Shree Swami Samarth")
print("Name: Sakshi Deshmukh")
print("Roll No: 14")

def Exp1():
    list = ["Name", "Surname", "@#", 3.14, 22]
    print("List contents following elements")
    for i in list:
        print(i)


def Exp2():
    str1 = input("Enter First String: ")
    str2 = input("Enter Second String: ")

    concat = str1 + " " + str2
    print("Concatenated String =", concat)

    upper = concat.upper()
    print("Upper Case of Concatenated String =", upper)

    lower = concat.lower()
    print("Lower Case of Concatenated String =", lower)

    substring = concat[1:3]
    print("Substring of Concatenated String =", substring)

    split = concat.split()
    print("After Splitting the Concatenated string =", split)


def Exp3():
    item = input("Enter your five items you want to purchase from the grocery shop with spaces: ")
    items = item.split()
    print("Your Items in String =", item)
    print("Your items in list are", items)

    print(" ")
    items.append(input("Enter one more item to append in the list: "))
    print("Your items after appending the new item to it:", items)

    print("Enter one more item to insert it at [2] position:")
    insert_item = input().strip()
    items.insert(2, insert_item)
    print("Your items after inserting the new item at [2] position:", items)

    rem_item = input("Enter the item you want to remove: ").strip()
    items.remove(rem_item)
    print(f"Your items after removing '{rem_item}' item:", items)


def Exp4():
    tup = tuple(input("Enter marks of students in class 2R (comma separated and include one 100 marks): ").split(","))
    print("Tuple is =", tup)

    mark = tup.count("100")
    print(f"Total {mark} students of 2R got 100 marks")

    roll = tup.index("100")
    print(f"So, Roll no {roll} got A grade")


def Exp5():
    set1 = set(input("Enter total animals in section A of the Zoo (comma separated): ").split(","))
    set2 = set(input("Enter total animals in section B of the Zoo (comma separated): ").split(","))

    print(f"Set A contains {set1} animals")
    print(f"Set B contains {set2} animals")

    print("Total animals in the Zoo =", set1.union(set2))
    print("Common animals from both sections =", set1.intersection(set2))


def Exp6():
    my_dict = {}
    n = int(input("How many key-value pairs do you want to add to the dictionary? "))
    for i in range(n):
        key = input("Enter Key: ")
        value = input("Enter Value: ")

        my_dict[key] = value
        print("The dictionary is =", my_dict)

    print("All Keys from the dictionary =", my_dict.keys())
    print("All the values from the dictionary =", my_dict.values())
    print("All items in the dictionary =", my_dict.items())

    remove_key = input("Enter a key to remove from the dictionary: ")
    if remove_key in my_dict:
        remove_value = my_dict.pop(remove_key)
        print(f"Removed key {remove_key} with value {remove_value}")
    else:
        print(f"Key {remove_key} not found in the dictionary")

    print("The updated dictionary is:")
    print(my_dict)


def Exp7():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    num3 = input("Enter third number: ")

    if num1 > num2 and num1 > num3:
        print(f"{num1} is Largest")

    elif num2 > num3:
        print(f"{num2} is Largest")

    else:
        print(f"{num3} is Largest")


def Exp8():
    fact = 1
    num = int(input("Enter the number to find its factorial: "))
    for i in range(1, num + 1):
        fact *= i

    print(f"Factorial of {num} is =", fact)


def Exp11():
    dist = int(input("Enter distance in km: "))
    new_dist = 1000 * dist
    print(f"The distance of {dist} km in meters =", new_dist)


def Exp12():
    no = int(input("Enter any number to check if it is prime or not: "))
    if no > 1:
        for i in range(2, no):
            if no % i == 0:
                print(f"{no} is not a Prime Number")
                break
        else:
            print(f"{no} is a Prime Number")
    else:
        print(f"{no} is not a Prime Number")

while True:
    # Print the list of experiments only once
    print("\nList of Experiments")
    print("1. Write a python program to store data in a list and print the list")
    print("2. Write a program to create, concatenate, and print a string and access substring from a given string")
    print("3. Write a python program to create, append, and remove a list in python")
    print("4. Write a program to demonstrate the working with tuples in python")
    print("5. Write a program to demonstrate the working with sets in python")
    print("6. Write a program to demonstrate the working with dictionaries in python")
    print("7. Write a program to find the largest of three numbers")
    print("8. Write a program to find the factorial of a number using a function")
    print("11. Write a program to convert km to m")
    print("12. Write a program to check if a given number is prime or not")


    try:
        choice = int(input("\nEnter the experiment number you want to perform (1-12 excluding 9 and 10): "))
        if choice == 1:
            print("\nExperiment no 1")
            Exp1()
        elif choice == 2:
            print("\nExperiment no 2")
            Exp2()
        elif choice == 3:
            print("\nExperiment no 3")
            Exp3()
        elif choice == 4:
            print("\nExperiment no 4")
            Exp4()
        elif choice == 5:
            print("\nExperiment no 5")
            Exp5()
        elif choice == 6:
            print("\nExperiment no 6")
            Exp6()
        elif choice == 7:
            print("\nExperiment no 7")
            Exp7()
        elif choice == 8:
            print("\nExperiment no 8")
            Exp8()
        elif choice == 11:
            print("\nExperiment no 11")
            Exp11()
        elif choice == 12:
            print("\nExperiment no 12")
            Exp12()
        else:
            print("Invalid experiment number! Please select between 1 to 12, excluding 9 and 10.")
            continue

        # Ask for continuation
        cont = input("\nDo you want to continue? (y/Y to continue, any other key to exit): ")
        if cont.lower() != 'y':
            print("Thank you!")
            break
    except ValueError:
        print("Please enter a valid experiment number.")
