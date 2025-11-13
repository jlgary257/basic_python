from logging import setLoggerClass

from breakpoint import print_hi
from print_datatype import print_datatype
from selection import cat_fatness, cat_inner_select

name = "Jojo Gary" #str
age = 23#int
weight = 100.3 #float
food = ["cat food", "chicken"] #list
isFat = True #boolean


if __name__ == '__main__':
    print_datatype(food)
    cat_fatness(weight)
    cat_inner_select(age)
