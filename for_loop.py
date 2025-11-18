def for_animal(words):
    for w in words:
        print(w, len(w))

def for_link(links):
    for l,status in links.copy().items(): #to call linked list values
        if status != 'cat':
            print(l, ' : ', status)

#RANGES
def num_range(num):
    for i in range(num):
        print(i)
def range_list(s,l):
    print(list(range(s, l)))

def range_word(list):
    for i in range(len(list)):
        print(i,list[i])