def is_palindrome(s):
    for i in range(0,int(len(s)/2)-1):
        if s[i] != s[len(s)-(i+1)]:
            print ("Not palindrome!")
            return False
    print ("Palindrome!")
    return True

string = input("Input a string: ")
is_palindrome(string)
