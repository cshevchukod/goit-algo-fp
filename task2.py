# task2.py - Завдання 2

import turtle


def pythagoras_tree(t, level, length):
    if level == 0:
        return

    # стовбур/гілка
    t.forward(length)

    # ліва гілка
    t.left(45)
    pythagoras_tree(t, level - 1, length * 0.7)

    # права гілка
    t.right(90)
    pythagoras_tree(t, level - 1, length * 0.7)

    # повертаємось у початковий напрямок і назад
    t.left(45)
    t.backward(length)


def task2():
    level = int(input("Вкажіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.title("Дерево Піфагора")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # старт знизу і дивимось вверх
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()

    pythagoras_tree(t, level, 120)

    screen.mainloop()


if __name__ == "__main__":
    task2()
