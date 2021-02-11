from random import choice
e=["a","b","r","g","p","t","s","d"]
w=choice(e)
print("welcome to this great game")
print("ok lets star whit letter",w)
r=input("esm:")
t=input("shahr:")
l=input("keshvar:")
k=input("heyvan:")
m=input("vasayel:")
R=r[0]
T=t[0]
L=l[0]
K=k[0]
M=m[0]
j=0
if R==w:
    j=j+20
if T==w:
    j=j+20
if L==w:
    j=j+20
if K==w:
    j=j+20
if M==w:
    j=j+20
print("your score is:",j)