s = 1
l = 100
num_list = []

for i in range(s,l):
    for x in range(2,i):
        if i % x == 0:
            #print(i, ' equal to ', x, ' * ', i//x)
            break
    else:
         num_list.append(i)
         #print(i)


def show_array(num_list):
    for i in num_list:
        print(i)

show_array(num_list)