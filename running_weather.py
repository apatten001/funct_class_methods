
temp = int(input("What is the current temperature in F°?: "))


def running_weather():
    if temp > 48 and temp < 52:
        print("This is a perfect temperature to set a record!")
    elif temp > 35 and temp < 48:
        print("This is good running weather to perform an optimal run")
    elif temp > 49 and temp < 75:
        print("This temp may have you perspire more than usual.")
    else:
        print("Run at your own risk!")

running_weather()




