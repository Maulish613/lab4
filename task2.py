import string
from collections import Counter
fin = open('pg2542.txt')
count = 0
unique=[] 
for i in fin:
    words = i.split()
    for word in words:
        white_space = string.whitespace
        punctuation = string.punctuation
        word = word.strip(white_space + punctuation)
        new_word = ''
        for j in word:
            printing_word = string.printable
            if j in printing_word:
                new_word+= j
                count+=1
        unique.append(new_word)
        #print(new_word)
 
#print(set(unique))
#print(count)

frequent_words = dict(Counter(unique))

#print(frequent_words)    
print(type(frequent_words))

c = Counter(frequent_words)
print(c.most_common(20))
    