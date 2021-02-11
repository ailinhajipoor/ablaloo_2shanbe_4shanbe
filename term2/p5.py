import turtle
turtle.bgcolor("blue")
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.penup() # قلم را از روی کاغذ برمیدارد
turtle.forward(-200)
turtle.pendown()#قلم را روی کاغذ میگذارد
turtle.color("red")
turtle.begin_fill()#آغاز رنگ کردن
turtle.circle(100)
turtle.end_fill()#پایان رنگ کردن
turtle.done()