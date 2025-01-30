# Step 1 : Install Python extension for vscode
# Step 2 : Go to Run and Debug in left hand side 
# Step 3 (optional): Install the json file for debugging - It will create a new folder called .vscode 
# Step 4 : Click Run and Debug - Select Python file. 
# Step 5 (optional) : If the above step4 does not work, click ctrl + shift + p



# languages = ['Swift', 'Python', 'Go', 'C++']
# for lang in languages:
#     if lang == 'Go':
#         break
#     print(lang)



# languages = ['Swift', 'Python', 'Go', 'C++']
# for lang in languages:
#     if lang == 'Go':
#         continue
#     print(lang)



# num = 10
# if num > 0:
#     if num % 2 == 0:
#         print("The number is positive and even.")
#     else:
#         print("The number is positive but odd.")
# else:
#     print("The number is not positive.")



# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username == "admin":
#     if password == "password":
#         print("Login successful! Welcome, admin.")
#     elif password == "12345":
#         print("Weak password. Please reset your password.")
#     else:
#         print("Incorrect password. Please try again.")
# else:
#     if username == "guest":
#         if password == "guest":
#             print("Login successful! Welcome, guest.")
#         else:
#             print("Incorrect password. Please try again.")
#     else:
#         print("Unknown user. Please try again.")


# def moderate_comment(comment):
#     profanity_list = ["badword1", "badword2", "badword3"]
#     for word in profanity_list:
#         if word in comment.lower():
#             return "Comment rejected: Contains profanity."
#     return "Comment approved."

# comment1 = "This is a great article!"
# comment2 = "This is a terrible article, full of badword1."
# print(moderate_comment(comment1))
# print(moderate_comment(comment2))


# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
# print("Recursion Example Results:")
# tri_recursion(6)



# def factorial(number):
#     if not isinstance(number, int):
#         raise TypeError("The number must be whole.")
#     if number < 0:
#         raise ValueError("The number must be non-negative.")
#     #Factorial calculation
#     def inner_factorial(number):
#         if number <= 1:
#             return 1
#         return number * inner_factorial(number - 1)
#     return inner_factorial(number)
#  factorial(4)



