#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.lower()=="admin" and password=="12345":
        return "Access granted"
    else:
        return "Access denied"
    pass

def hows_the_weather(temperature):
    # your code here
    if temperature<40:
        response = "brisk"
    elif temperature>=40 and temperature<=65:

        response = "a little chilly"

    elif temperature>65 and temperature <=85:

        response = "perfect"
    else:
       response = "too dang hot"
    
    return f"It's {response} out there!"
    pass

def fizzbuzz(num):
    # your code here
    if num%3==0 and num%5==0:
        response = "FizzBuzz"
    elif num%3==0:
        response = "Fizz"
    elif num%5==0:
        response = "Buzz"
    else:
        response = num
    return response
    pass

def calculator(operation, num1, num2):
    # your code here
    calculator ={
        '+': num1+num2,
        '-': num1-num2,
        '*': num1*num2,
        '/': num1/num2
    }
    return calculator.get(operation, print("Invalid operation!"))
    pass
