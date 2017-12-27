import time


Lifts = "Bench,Deadlift,Squat,Row,Clean".split(",")

# Using a funtion within a function as well as using a global variable
for lift in Lifts:

    def barbell():
        added = int(input("How many pounds did you add to the Barbell for the {}: ".format(lift) + "\n"))
        weight = 45
        return added+weight


    # sentence = ("The bar weighs {}lbs and you added {}lbs. Therefore your total amount on the barbell was {}lbs ".format(weight, added , total))
    # print(sentence)

def bench():
    for lift in Lifts:
        print("On the {}, You've {} {}lbs on ".format(lift,(lift+"ed"),barbell()) + str(time.ctime())+"\n")


print(bench())






