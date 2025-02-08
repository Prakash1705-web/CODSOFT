import random 
import string

def pwd(user_length):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digit = string.digits
    
    password = lower_case + upper_case + digit
    
    pass_word = ''.join (random.choices(password, k = user_length))
    
    return pass_word
    
user = int(input("Enter the length of the password : "))
    
generated_pwd = pwd(user)

print("Generated Password : ", generated_pwd)
