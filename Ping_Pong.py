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

# создаем ракетки

# левая ракетка

left_rocket = turtle.Turtle()
left_rocket.color('white')  # цвет ракетки
left_rocket.shape('square')  # создаем форму ракетки
left_rocket.shapesize(stretch_wid=4.8, stretch_len=0.6)  # размер ракетки
left_rocket.penup()
left_rocket.goto(-470, 0)

# правая ракетка

right_rocket = turtle.Turtle()
right_rocket.color('white')  # цвет ракетки
right_rocket.shape('square')  # создаем форму ракетки
right_rocket.shapesize(stretch_wid=4.8, stretch_len=0.6)  # размер ракетки
right_rocket.penup()
right_rocket.goto(470, 0)


def move_up_left_rocket():
    """
    Метод движения вверх и условие которое не дает нам уйти за границы стола.
    :return:
    """
    y = left_rocket.ycor() + 45
    if y > 250:
        y = 250
    left_rocket.sety(y)


def move_down_left_rocket():
    """
    Метод движения вниз и условие которое не дает нам уйти за границы стола.
    :return:
    """
    y = left_rocket.ycor() - 45
    if y < -250:
        y = -250
    left_rocket.sety(y)


def move_up_right_rocket():
    """
    Метод движения вверх и условие которое не дает нам уйти за границы стола.
    :return:
    """
    y = right_rocket.ycor() + 45
    if y > 250:
        y = 250
    right_rocket.sety(y)


def move_down_right_rocket():
    """
    Метод движения вниз и условие которое не дает нам уйти за границы стола.
    :return:
    """
    y = right_rocket.ycor() - 45
    if y < -250:
        y = -250
    right_rocket.sety(y)


window.listen()  # позволит понимать окну нажатие некоторых кнопок
window.onkeypress(move_up_left_rocket, 'w')
window.onkeypress(move_down_left_rocket, 's')
window.onkeypress(move_up_right_rocket, 'i')
window.onkeypress(move_down_right_rocket, 'k')

window.mainloop()  # чтобы наше окно сразу не закрывалось
