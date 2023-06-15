def checkpalindrome(string): #сложность O(1)
    if string[::-1]==string:
        return True
    else:
        return False
print(checkpalindrome('шалаш'))
