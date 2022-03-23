from collections import Counter


words = ['cat','dog','cat','unicorn','lizard', 'lizard']


counts = Counter(words)
#print(counts)


def returnOne(l):
    c = Counter(l)
    b = False
    for i in c:
        key = i
        value = c[i]
        if(value == 1):
            print(key)

returnOne(words)
