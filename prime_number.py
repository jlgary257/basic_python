
def prime_no(list, s,l):
    for i in range(s,l):
        for x in range(2,i):
            if i % x == 0:
                #print(i, ' equal to ', x, ' * ', i//x)
                break
        else:
             list.append(i) #to add value to an array
             #print(i)
    show_array(list)


def show_array(num_list):
    for i in num_list:
        print(i)

