#from cgi importform
text = "hello world"
print(text)
text= "hello world 2"
print(text)
print(text[4])
print(len(text)) # what is the lenght of the text
text= ""
print(len(text))
text="Bob"
print(text[-1]) #last charaxter in the strint
print(text[-3])

#print(text[3]) #this is an error
print(text[6//3])

#you can add 2 strings
s1="hello"
s2= "bye"
print(s1 + s2)
print(s1*4)

#string is iteriable, you can use for over it
s1= "hello my name is bob"
for c in s1:
    print(c)

s1= "i like to give hi fives"
#print thsi string . but replace "i" with y
#Y lykes to gyve hy fyves
s1_new= ""
for c in s1:
    if c=="i":
        s1_new +="y"
    elif c=="I":
        s1_new +="Y"
    else:
        s1_new= s1_new +c
        print(s1_new)

s1= "I like to give hi fives"
for c in s1:
    if c=="i":
        print("y", end="")
    elif c=="I":
        print("Y", end="")
    else:
        print(c, end="")