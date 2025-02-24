# 1. Encapsulation in Personal Budget Management
# Objective: The aim of this assignment is to reinforce the understanding of encapsulation in Python, 
# focusing on the use of private attributes and getters and setters.

# Problem Statement: You are required to build a Personal Budget Management application. 
# The application will manage budget categories like food, entertainment, utilities, etc., 
# ensuring that budget details remain private and are accessed or modified through public methods.

# Task 1: Define Budget Category Class Create a class `BudgetCategory` with private attributes for category name and allocated budget. 
# - Initialize these attributes in the constructor.

# - Expected Outcome: A `BudgetCategory` class capable of storing category details securely.

# Task 2: Implement Getters and Setters - Write getter and setter methods for both the category name and the allocated budget. 
# - Ensure that the setter methods include validation (e.g., budget should be a positive number).

# - Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.

# Task 3: Add Budget Functionality Implement a method to add expenses to a category and adjust the budget accordingly. 
# - Validate the expense amount before making deductions from the budget.

# Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

# Task 4: Display Budget Details Create a method to display the details of a budget category, 
# including the name, allocated budget, and remaining budget after expenses.

# Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.

# Code Examples:

class PS5Budget:
    def __init__(self, member_name, allocated_budget):
        # Intialize the memeber's name and their alocated budget.
        self.__member_name = member_name
        if allocated_budget <= 0:
            raise ValueError("Allocated budget must be a positive number.")
        self.__allocated_budget = allocated_budget
        # Initailize the remaning budget to be the same as the allocated budget.
        self.__remaining_budget = allocated_budget

    # Getter for the memeber's name.
    def get_member_name(self):
        return self.__member_name

    # Setter for the memeber's name.
    def set_member_name(self, new_name):
        self.__member_name = new_name

    # Getter for the alocated budget.
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for the alocated budget with validation.
    def set_allocated_budget(self, new_budget):
        if new_budget <= 0:
            raise ValueError("Allocated budget must be a positive number.")
        self.__allocated_budget = new_budget
        # Reset the remaning budget to the new alocated budget.
        self.__remaining_budget = new_budget

    # Method to add an expence.
    def add_expense(self, amount):
        # Check that the expence ammount is a positive number.
        if amount <= 0:
            print("Expense amount must be a positive number!")
            return
        
        # Check if there's enuf remaning budget.
        if amount > self.__remaining_budget:
            print("Insufficient funds in budget!")
            return
        
        # Deduct the expence from the remaning budget.
        self.__remaining_budget -= amount
        print(f"Expense of {amount} has been added successfully.")

    # Method to display the budjet details.
    def display_category_summary(self):
        print("\nBudget Category Summary:")
        print(f"Member Name       : {self.__member_name}")
        print(f"Allocated Budget  : {self.__allocated_budget}")
        print(f"Remaining Budget  : {self.__remaining_budget}")


# Testing the PS5Budget class
if __name__ == '__main__':
    # Create an instance of PS5Budget with a memeber name and an alocated budget.
    member_budget = PS5Budget("Alice", 1000)
    
    # Display the initial budjet details.
    print("Initial Budget Details:")
    member_budget.display_category_summary()
    
    # Test adding a valid expence.
    print("\nAdding an expence of 200:")
    member_budget.add_expense(200)
    member_budget.display_category_summary()
    
    # Test adding an invalid expence (too high).
    print("\nTrying to add an expence of 900 (should fail due to insufficient funds):")
    member_budget.add_expense(900)
    member_budget.display_category_summary()
    
    # Test adding an invalid expence (non-positive).
    print("\nTrying to add an expence of -50 (should be invalid):")
    member_budget.add_expense(-50)
    member_budget.display_category_summary()


    # Constructor and private attributes
    # ...

    # Getters and setters for category name and budget
    # ...


        # ...

    #ef display_category_summary(self):
        # Method to display the budget category details
        # ...

#ood_category = BudgetCategory("Food", 500)
#ood_category.add_expense(100)#
#ood_category.display_category_summary()


# NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs. If there are classes/objects, make sure they are instantiated and the methods are called.

# The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.