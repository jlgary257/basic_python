from contextlib import asynccontextmanager


def cat_fatness(weight):
    if weight >= 20:
        print("Very FAT CAT")
    elif weight >=10 & weight < 20:
        print("Average size")
    else:
        print("Small cat")


def cat_inner_select(age):
    if age >= 20:
        if age <= 25:
            print("Moderate Old")
        else:
            print("very Old Cat")
    else:
        print("Young Cat")
