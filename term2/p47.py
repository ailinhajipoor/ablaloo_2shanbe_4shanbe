from random import choice
from time import sleep
player=[]
while 1==1:
    a=input("name : ")
    if a=="end":
        break
    else:
        player.append(a)
jayezehe=[]
while 1==1:
    a=input("jayzeha : ")
    if a=="end":
        break
    else:
        jayezehe.append(a)
print( "1  .   .    .")
sleep(1)
print( "2  .   .    .")
sleep(1)
print( "3  .   .    .")
sleep(1)
print("----------------------------------")
for i in range(20):
    print(choice(player),"= >" ,choice(jayezehe))


