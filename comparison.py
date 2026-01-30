#bc string are immutable

s= "cat"
#s[0]= "r"
s="r" +s[1:]
print(s)

s1= "BOB"
s2= "bannana"
print(s1<s2)

s1="BOB"
s2= 'bob'
print(s1> s2)


# in operator checks is a string is part of another
print("anna in bannana")# true
print("Ana in bannana")# false