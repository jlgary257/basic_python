
def palindrome(m, n, count=0):
    for x in range(m,n+1):
        # to check palindrome
        if str(x) == str(x)[::-1]: #reverses string
            print(x)
            count +=1
    print(count)