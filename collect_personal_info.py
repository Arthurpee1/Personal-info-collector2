Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def collect_personal_info():
...     print("---- Personal Information Collector ----\n")
...     name = input("Please enter your full name: ")
...     #Age input with validation
...     while True:
...         try:
...             age = int(input("Enter your age: "))
...             break
...         except ValueError:
...             print("Please enter a valid number for age.")
...             gender = input("Gender (M/F?Other): ")
...             email = input("Email Address: ")
...             phone = input("Phone Number: ")
...             favorite_color = input("Favorite Color: ")
...             # Student status input
...             student_input("Are you a student? (yes/no): ").strip().lower()
...             is_student = student_input == "yes"
...             #Diplay collected information
...             print("\n----- Displaying Collected Information -----")
...             print(f"Name: {name}")
...             print(f"Age: {age}")
...             print(f"Gender: {gender}")
...             print(f"Email: {email}")
...             print(f"Phone: {phone}")
...             print(f"Favorite Color: {favorite_color}")
...             print(f"Student Status: {is_student}")
... 
...             
>>> #Run the function
...             
>>> 
========================================================================== RESTART: Shell =========================================================================
>>> #Run the function
>>> 
========================================================================== RESTART: Shell =========================================================================
