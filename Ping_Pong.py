import turtle
from random import choice, randint

window = turtle.Screen()  # создадим окно и положем в переменную window
window.title('Ping-Pong')  # создадим заголовок нашего окна
window.setup(width=0.7, height=0.7)  # создадим размеры нашего окна
window.bgcolor('#1A4780')  # цвет нашего фона окна
window.tracer(2)

# создаем стол

table = turtle.Turtle()
table.speed(0)  # скорость отрисовки стола
table.color('#228B22')

# рисуем стол по координатам

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
table.setheading(270)  # делает направление вниз (270 в turtle всегда вниз)
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
left_rocket.shapesize(stretch_len=0.6, stretch_wid=4.8)  # размер ракетки
left_rocket.penup()
left_rocket.goto(-470, 0)

# правая ракетка

right_rocket = turtle.Turtle()
right_rocket.color('white')  # цвет ракетки
right_rocket.shape('square')  # создаем форму ракетки
right_rocket.shapesize(stretch_len=0.6, stretch_wid=4.8)  # размер ракетки
right_rocket.penup()
right_rocket.goto(470, 0)


def move_up_left_rocket():
    """
    Метод движения вверх и условие, которое не дает нам уйти за границы стола.
    :return:
    """
    y = left_rocket.ycor() + 45
    if y > 250:
        y = 250
    left_rocket.sety(y)


def move_down_left_rocket():
    """
    Метод движения вниз и условие, которое не дает нам уйти за границы стола.
    :return:
    """
    y = left_rocket.ycor() - 45
    if y < -250:
        y = -250
    left_rocket.sety(y)


def move_up_right_rocket():
    """
    Метод движения вверх и условие, которое не дает нам уйти за границы стола.
    :return:
    """
    y = right_rocket.ycor() + 45
    if y > 250:
        y = 250
    right_rocket.sety(y)


def move_down_right_rocket():
    """
    Метод движения вниз и условие, которое не дает нам уйти за границы стола.
    :return:
    """
    y = right_rocket.ycor() - 45
    if y < -250:
        y = -250
    right_rocket.sety(y)


#  создаем шар

ball = turtle.Turtle()
ball.shape('circle')  # делаем форму шара круглой
ball.color('white')  # цвет шара
ball.speed(0)
ball.dx = 3  # движение шара по x
ball.dy = 3  # движение шара по y
ball.penup()  # чтобы шар не оставлял след

window.listen()  # позволит понимать окну нажатие некоторых кнопок
window.onkeypress(move_up_left_rocket, 'w')
window.onkeypress(move_down_left_rocket, 's')
window.onkeypress(move_up_right_rocket, 'i')
window.onkeypress(move_down_right_rocket, 'k')

while True:  # бесконечный цикл движения нашего шарика
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:  # условие дли отскока шарика от верхней стенки
        ball.dy = -ball.dy

    if ball.ycor() <= -290:  # условие дли отскока шарика от нижней стенки
        ball.dy = -ball.dy

    if ball.xcor() >= 490:  # условие при котором мяч возвращается в исходное положение стола в центре
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    if ball.xcor() <= -490:  # условие при котором мяч возвращается в исходное положение стола в центре
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    # логика отбивания шарика ракеткой
    # левая ракетка

    if ball.ycor() >= left_rocket.ycor() - 50 and ball.ycor() <= left_rocket.ycor() + 50 \
            and ball.xcor() >= left_rocket.xcor() - 5 and ball.xcor() <= left_rocket.xcor() + 5:
        ball.dx = -ball.dx
    # правая ракетка
    if ball.ycor() >= right_rocket.ycor() - 50 and ball.ycor() <= right_rocket.ycor() + 50 \
            and ball.xcor() >= right_rocket.xcor() - 5 and ball.xcor() <= right_rocket.xcor() + 5:
        ball.dx = -ball.dx



window.mainloop()  # чтобы наше окно сразу не закрывалось
