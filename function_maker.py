# functions use def to define the function
# and the function is lower case
import sys


def addNum(num1,num2):
    newnum = num1 + num2
    return newnum


print(addNum(3,5))

def subNum(num1,num2):
    newnum = num1 - num2
    return newnum


print(subNum(3,5))

def mult_Num(num1,num2):
    newnum = num1 + num2
    return newnum


print(mult_Num(3,5))

def divide_Num(num1,num2):
    newnum = num1 + num2
    return newnum


print(divide_Num(3,5))


def welcome():
    print("What is your name")
    name = sys.stdin.readline()
    print('Welcome', name)

welcome()

# def goodbye

