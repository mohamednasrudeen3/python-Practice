def moveash(s):
    count = s.count("#")
    str1 = s.replace("#","")
    ans ='#'* count+str1
    return ans
s= input()
print(moveash(s))