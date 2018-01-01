
# Working with the file object sys

separator = ", "

#using with as a context manager to automatically close out a file

with open("text.txt", 'a') as f:
    f.write("\n" + input("What is your Name?: ") + separator + input("What is your email address?: "))

print(f.closed)

with open("/Users/arnold/Desktop/quotes.txt",'r') as f:
    f_contents = f.read()
    print(f_contents)

print(f.closed)

# readlines creates a list of the lines in the file read
# readline just reads the first line of the file

with open("/Users/arnold/Desktop/quotes.txt",'r') as f:
    f_contents = f.readline()
    print(f_contents,end='')

# prints each line in the file
with open("/Users/arnold/Desktop/quotes.txt",'r') as f:

    for line in f:
        print(line,end='')



