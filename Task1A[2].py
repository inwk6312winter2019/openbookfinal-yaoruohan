import string
def count_the_article():
        str1 = []
        fout = open('book1.txt', 'r')
        r = fout.readlines()

        for line in r:
            str2 = line.lower().strip(string.punctuation + string.whitespace)
            str1 += str2

        total = {}
        for word in str1:
            total[word] = total.get(word, 0) + 1
        words_t = len(str1)

        print('total number words is: ' + str(words_t))

print(count_the_article())