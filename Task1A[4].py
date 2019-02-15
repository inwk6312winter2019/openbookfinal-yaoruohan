import string
def character_word_count():
    fout = open('book1.txt','r')
    d = {}
    l = fout.split()

    for word in l:
        if (word[0] not in d.keys()):
            d[word[0]] = []
            d[word[0]].append(word)
        else:
            if(word not in d[word[0]]):
                d[word[0]].append(word)
    for k,v in d.items():
        print(k,":",v)






