print(dir("x"))
print(help("x". capitalize))
s= "bob ATE PIZZA"
print(s.capitalize())

print(s.count("A"))# 2 capitalized A in strig
s= "banana and another ana + an again"
print(s.count("ana"))

#find, finds the position of the frst occurency
s= "banana"
print(s.find("ana")) #ana is found from position 1# (s.find(sub:"ana", start:2))
print(s.find("ana", 2))

#replace, replace string inside string
print(s.replace("ana", "BOB"))
s = ("I, like: tp go out!")
print(s.split(" "))

#remove ounctuation from a sentance and extract words
punct= ",.!;"
for c in punct:
    s= s.replace(c, "")
    print(s.split())