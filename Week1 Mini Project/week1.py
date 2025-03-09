# Week 1 Mini Project - Python Fundamentals

# Question 1: User Data Collector
def collect_user_data():
    user_data = {}
    user_data["name"] = input("Enter your name: ")
    user_data["age"] = input("Enter your age: ")
    user_data["email"] = input("Enter your email: ")
    user_data["favorite_number"] = input("Enter your favorite number: ")

    # Validate email
    if "@" in user_data["email"] and "." in user_data["email"]:
        print("\nUser Data Collected Successfully:")
        for key, value in user_data.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Invalid email! Please enter a valid email.")

# Question 2: Even or Odd?
def is_even(number):
    return number % 2 == 0

def check_even_odd():
    num = int(input("\nEnter a number to check if it's even or odd: "))
    if is_even(num):
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")

# Question 3: Temperature Converter
def convert_temperature(temp, scale):
    if scale == "C":
        return (temp * 9/5) + 32  # Celsius to Fahrenheit
    elif scale == "F":
        return (temp - 32) * 5/9  # Fahrenheit to Celsius
    else:
        return None  # Invalid input

def temp_conversion():
    temp = float(input("\nEnter the temperature: "))
    scale = input("Enter the scale (C for Celsius, F for Fahrenheit): ").upper()
    
    converted_temp = convert_temperature(temp, scale)
    if converted_temp is not None:
        print(f"Converted Temperature: {converted_temp:.2f}°")
    else:
        print("Invalid scale entered!")

# Question 4: Finding Min & Max
def find_max_min(numbers_list):
    return max(numbers_list), min(numbers_list)

def min_max_numbers():
    numbers = []
    print("\nEnter 5 numbers:")
    for i in range(5):
        num = int(input(f"Number {i+1}: "))
        numbers.append(num)
    
    max_value, min_value = find_max_min(numbers)
    print(f"Maximum Number: {max_value}")
    print(f"Minimum Number: {min_value}")

# Question 5: Student Data Manager
def student_data_manager():
    students = []
    
    print("\nEnter details for 3 students:")
    for _ in range(3):
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        students.append((name, age, grade))
    
    student_dict = {name: (age, grade) for name, age, grade in students}
    
    print("\nStudent Data Dictionary:")
    print(student_dict)

# Question 6: Inventory Management System
def update_inventory(inventory_dict, item, quantity):
    if item in inventory_dict:
        inventory_dict[item] = max(0, inventory_dict[item] + quantity)
    else:
        print(f"Item '{item}' not found in inventory.")

def inventory_manager():
    inventory = {
        "apple": 10,
        "banana": 15,
        "orange": 12,
        "mango": 8,
        "grapes": 20
    }

    print("\nCurrent Inventory:")
    print(inventory)

    for _ in range(3):
        item = input("\nEnter item to update: ").lower()
        quantity = int(input("Enter quantity (+ to add, - to remove): "))
        update_inventory(inventory, item, quantity)

    print("\nUpdated Inventory:")
    print(inventory)

# Main Function to Run All Tasks
def main():
    collect_user_data()
    check_even_odd()
    temp_conversion()
    min_max_numbers()
    student_data_manager()
    inventory_manager()

# Run the main function
if __name__ == "__main__":
    main()
