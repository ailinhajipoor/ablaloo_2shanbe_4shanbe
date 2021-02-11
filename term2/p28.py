import turtle

t = turtle
answer = input("circle or square?")

t.pensize(10)
# sakhte turtel
t.pensize(10)
t.color('cyan', 'cyan')
t.shapesize(3)
t.shape('turtle')
# a=random.randint(1,2)
# print(a)
if answer == "square":
    shoa = input("ضلع را وارد کن")
    shoa = int(shoa)
    for i in range(4):
        t.forward(shoa)
        t.right(90)

if answer == "circle":
    shoa = input("شعاع را وارد کن")
    shoa = int(shoa)
    t.circle(shoa)
t.done()
