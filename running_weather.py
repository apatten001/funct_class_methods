
temp = int(input("What is the current temperature in F°?: "))
condition = input("Is it rainy, windy, or clear outside?: ")

class BestTime:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def running_weather(self):

        if temp > 48 and temp < 52:
            print("This is a perfect temperature to set a record!")
        elif temp > 35 and temp < 48:
            print("This is good running weather to perform an optimal run")
        elif temp > 49 and temp < 75:
            print("This temp may have you perspire more than usual.")
        else:
            print("Run at your own risk!")

    def conditions(self):
        if condition == "rainy":
            print(f"{self.name},when its raining your clothes may weigh you down\
             causing you to slow down your pace.")
        elif condition == "windy":
            print(f"Depending on the way the wind blows {self.name}, it will increase or decrease your "
            "speed on average by 10%.")
        elif condition == "clear":
            print(f"{self.name}, you should have a good run ahead of you!")
        else:
            print("Depending on the conditions you may want to wait to run")



Arnold = BestTime("Arnold", 31)

Arnold.running_weather()
Arnold.conditions()