javab=input("type your age: ")
if int(javab)>50 :
    print("senet ziade .to nemitooni in bazi ro anjam bedi")
else:

    a=open("new.txt", "a")
    a.write(javab)
    a.close()

