#importing the function we need to get the output needed
import random


#this variable consist of all punctuations, and cases of letters
cases = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_-+=~`,.:;/1234567890'

#generates a number between 12 and 20
password_len = random.randint(12, 20)

#the passoword I will be adding onto
password = ''

#a loop to create a password between the length of 12 to 20
for char in range(password_len):
  #randomly generating a character each time a new iteration appears 
  password_char = random.choice(cases)
  #this conditional prevents duplicated characters in the password
  if password_char not in password:
    #concatenating the characters together
    password = password_char + password



#printing the password 
print("Here is your password: {}".format(password))

  


  
  