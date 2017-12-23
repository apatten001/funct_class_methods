
# *args and *kwargs allow you to make multiple arguments or keyword arguments
# make sure you use *

class Christmas():

    def christmas_info(*args, **kwargs):
        print(args)
        print(kwargs)


christmas_list = ["stereo", "Headphones","Aux Cord",'tree']

christmas_dict = {"Arnold":"Nice", "Jen": "Naughty"}

Arnold = Christmas

Arnold.christmas_info(*christmas_list,**christmas_dict)

Arnold.christmas_info("socks","hat","gym_bag", "shoes",**{"FRUIT":"apple","Cowboy":"Horse"})