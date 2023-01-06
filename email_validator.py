# # Email validation with string 
# email = input("Enter your email_id:- ")
# k, j, d = 0, 0, 0
# if len(email) >= 6:
#     if email[0].isalpha():
#         if ("@" in email) and (email.count("@") == 1):
#             if (email[-4] == ".") ^ (email[-3] == "."):
#                 for i in email:
#                     if i == i.isspace():
#                         k = 1
#                     elif i.isalpha():
#                         if i == i.upper():
#                             j = 1
#                     elif i.isdigit():
#                         continue
#                     elif i == "_" or i == "." or i == "@":
#                         continue
#                     else:
#                         d = 1
                                             
#                 if k == 1 or j == 1 or d ==1 :
#                     print("You have entered wrong email")

#                 else:
#                     print("You have entered correct email")
#         else:
#             print("@ Condition is failed")
#     else:
#         print("Condition is failed")
# else:
#     print("You have entered wrong email_id")
    

# Email validation with RegEx

# a-z
# 0-9
# . _ time 1
# @ time 1
#. 2,3 times

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your mail:- ")

if re.search(email_condition, user_email):
    print("You have entered right email")
else:
    print("You have entered Wrong email")