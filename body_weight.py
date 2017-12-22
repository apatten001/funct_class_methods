name = input("What is your name?: ")
body_weight = input("Please enter your body weight: ")


class BodyWeight():
    """THis class will return a persons body weight in lbs or kg."""


    def __init__(self, age=None, height=None):
        self.age = age
        self.height = height



    def weight_lbs(self):

        print("{}, Your weight in pounds is {}".format(name, body_weight))

    def weight_kg(self):

        kilos = float(body_weight)/2.2

        print("%s, Your weight in Kilograms is %.2f" %(name, kilos))


client_1 = BodyWeight(31,73)
client_2 = BodyWeight()


client_1.weight_lbs()
client_1.weight_kg()
print("\n")
client_2.weight_lbs()
client_2.weight_kg()



