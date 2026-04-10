import turtle

def draw_square(x, y, side_length, color):
    """
    function drawing a square
    :param x: start x pos
    :param y: start y pos
    :param side_length: length of the square
    :param color: color of the square
    :return: None
    """
    turtle.penup()
    turtle.goto(x, y)

    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pendown()

    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)

    turtle.end_fill()


def draw_circle(x, y, radius, color):
    """
    function drawing a circle
    :param x: center x position
    :param y: center y position
    :param radius: circle radius
    :param color: color of the circle
    :return: None
    """
    turtle.penup()
    turtle.goto(x, y - radius)

    turtle.fillcolor(color)
    turtle.begin_fill()

    turtle.pendown()
    turtle.circle(radius)
    turtle.end_fill()

def draw_star(x, y, size, color):
    """
    function drawing a star
    :param x: stride x position
    :param y: stride y position
    :param size: size of the star
    :param color: color of the star
    :return: None
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    turtle.fillcolor(color)
    turtle.begin_fill()

    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

    turtle.end_fill()

import turtle

def main():
    """
    main function drawing The ornament
    :return: None
    """
    turtle.speed(1000)
    turtle.penup()
    y = 0
    i = 1
    while i != 10:
        if i % 2 != 0:
            for x in range(-200, 200, 80):
                draw_square(x, y, 20, '#ff033e')
                draw_circle(x + 30, y + 10, 10, '#42aaff')
                draw_circle(x - 10, y + 10, 10, '#8b00ff')
                draw_star(x + 40, y + 12, 20, '#008000')

            y += 20
            i += 1
        else:
            for x in range(-180, 200, 80):
                draw_star(x - 40, y + 12, 20, '#008000')
                draw_square(x, y, 20, '#ff033e')
                draw_circle(x + 30, y + 10, 10, '#42aaff')
                draw_circle(x - 10, y + 10, 10, '#8b00ff')
            y += 20
            i += 1
    turtle.done()
main()
