import string
def unique_words():
    empty = []
    file = open("book1.txt", "r")
    for line in file:
        res = line.lower().strip(string.punctuation + string.whitespace)
        empty += res
    return empty

print(unique_words())


with open("Book1.text","r") as f1:
    l1 = f1.readline()
    word1 = line1.spilt()
with open("Book2.text","r") as f2:
    l2 = f2.readline()
    word2 = line2.spilt()
with open("Book3.text","r") as f3:
    l3 = f3.readline()
    word3 = line3.spilt()
unique_list1 = []
unique_list2 = []
unique_list3 = []

for i in word1:
  if i not in unique_list1:
           unique_list1.append(i)
        return unique_list1

for x in word2:
        if x not in unique_list2:
            unique_list2.append(x)
        return unique_list2

for h in word3:
        if h not in unique_list3:
            unique_list3.append(h)
        return unique_list3






