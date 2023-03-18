import turtle

window = turtle.Screen()  # создадим окно и положем в переменную window
window.title('Ping-Pong')  # создадим заголовок нашего окна
window.setup(width=0.7, height=0.7)  # создадим размеры нашего окна
window.bgcolor('#1A4780')  # цвет нашего фона окна

# создаем стол

table = turtle.Turtle()
table.speed(0)  # скорость отрисовки стола
table.color('#228B22')

# отриcовываем стол по координатам

# сам стол
table.begin_fill()
table.goto(-500, 300)
table.goto(500, 300)
table.goto(500, -300)
table.goto(-500, -300)
table.goto(-500, 300)
table.end_fill()  # закрашивает полностью наш стол

# отрисовываем рамку на столе белого цывета

table.goto(-500, 300)
table.color('white')
table.goto(500, 300)
table.color('white')
table.goto(500, -300)
table.color('white')
table.goto(-500, -300)
table.color('white')
table.goto(-500, 300)
table.color('white')

# ресуем разделительный пунктир по середине стола

table.goto(0, 300)
table.color('white')
table.setheading(270)  # делает направление вниз (270 в turttle всегда вниз)
for i in range(25):
    if i % 2 == 0:
        table.forward(24)
    else:
        table.up()
        table.forward(24)
        table.down()

table.hideturtle()
window.mainloop()  # чтобы наше окно сразу не закрывалось
