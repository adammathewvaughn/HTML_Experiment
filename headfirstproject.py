Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Welcome
      
SyntaxError: EOL while scanning string literal
>>> 
KeyboardInterrupt
>>> 
================================ RESTART: Shell ================================
>>> print("Welcome!")
g = input("Guess the number: ")
guess = int(g)
if guess == 5:
print("You win!")
else:
print("You lose!")
print("Game over!")