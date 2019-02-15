from collections import Counter
fin = open('book1.txt','book2.txt','book3.txt')
c = Counter()
for line in fin:
    words = line.split()
    c += Counter(words)
for words in c.most_common(20):
    print(words,end = '&')