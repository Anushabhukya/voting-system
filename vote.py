x=int(input("enter the no.of studuents in the class: "))
l=[]
for i in range(1,x+1):
    l.append(i)
print(l[0::])
s=int(input("enter no.of students participating in the competition: "))
l1=[]
for j in range(s):
    j=int(input("enter the roll.no of the student:"))
    print(j)
    l1.append(j)    
print(l1[0::])
l2=[]
for i in range(x):
    i=int(input("your vote is for: "))
    if i in l1: 
       l2.append(i)
    else:
       print("invalid vote ")   
       i=int (input("enter your vote: "))
       l2.append(i)
    print()   
print(l2) 
d={}
for i in l1:
    d[i]=l2.count(i)
    print("no.of votes for each one is: ",d)
    print()
print()
