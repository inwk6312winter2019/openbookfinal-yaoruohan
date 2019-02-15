import string

file = open('book1.txt')
my_str = file
words = my_str.split()
words = words.sorted()
for word in words:
    print(word)






