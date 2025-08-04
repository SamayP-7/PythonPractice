
def long_word(word):
    l2=[]
    for i in l1:
        if len(i)>len(word):
            l2.append(i)
    print(l2)



l1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']



long_word('Red')
long_word('Green')
long_word('Yellow')
