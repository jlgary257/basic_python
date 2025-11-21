from logging import setLoggerClass

from breakpoint import print_hi
from for_loop import for_animal, for_link, num_range, range_list, range_word
from print_datatype import print_datatype
from selection import cat_fatness, cat_inner_select

name = "Jojo Gary" #str
age = 23#int
weight = 100.3 #float
food = ["cat food", "chicken"] #list
isFat = True #boolean
words = ['cat','dog','lion','penguin','fish', 'eagle']
link_words = {'A':'cat','B':'dog','C':'cat','D':'penguin','E':'cat','F': 'eagle'}

if __name__ == '__main__':
    #print_datatype(food)
    #cat_fatness(weight)
    #cat_inner_select(age)
    for_animal(words)
    for_link(link_words)
    #num_range(10)
    #range_list(3,10)
    range_word(words)
    print(list(enumerate(words)))
