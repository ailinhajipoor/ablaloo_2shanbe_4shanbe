a=input("what's your name ?")
b=input("what's your last name ?")
c=input("tell me dsomething about yourself ?")
filename=a+".txt"
f=open(filename,"a")
f.write(a)
f.write("\n\n\n")
f.write(b)
f.write("\n\n\n")
f.write("--------------")
f.write("\n\n\n")
f.write(c)
f.close()