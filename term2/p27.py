import turtle
answer=input("circle or square ?")
if answer=="circle" :
    shoa=input("شعاع را وارد کن")
    shoa=int(shoa)
    turtle.circle(shoa)
    turtle.done()
if answer=="square":
    for i in range(0,4):
        turtle.forward(100)
        turtle.left(90)
    turtle.done()

