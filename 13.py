import turtle
t = turtle.Turtle()


def polyhedron(vertices: list, color: str) -> None:
    """
    Function, drawing polyhedron.

    :param vertices: a list consisting of the coordinates of the polyhedron's
    vertices. The function will traverse the vertices one by one
    :param color: fill color
    :param stop: accepts two arguments: 0 - close the window, 1 - leave it open
    (the default value is 0)

    :return: None
    """
    t.fillcolor(color)
    t.begin_fill()
    t.penup()
    t.goto(vertices[0])
    t.pendown()

    for vertex in vertices[1:] + [vertices[0]]:
        t.goto(vertex)

    t.end_fill()
    t.penup()

def square(vertices: list, color1: str, color2: str) -> None:
    polyhedron(vertices, color1)
    if vertices[1][1] > vertices[2][1]:
        vertices[1] = (vertices[1][0] - 20, vertices[1][1] - 20)
    else:
        vertices[1] = (vertices[1][0] - 20, vertices[1][1] + 20)
    polyhedron(vertices, color2)


def main():
    # Blue - '#0000ff'
    # light-blue - '#87cefa'
    # blue-gray - '#dbefff'
    square([(-200, 200), (-180, 200), (-180, 180)], '#0000ff', '#87cefa')
    square([(-180, 200), (-160, 200), (-160, 180)], '#87cefa', '#0000ff')
    square([(-160, 200), (-140, 200), (-140, 180)], '#dbefff', '#87cefa')
    square([(-140, 180), (-120, 180), (-120, 200)], '#87cefa', '#dbefff')
    square([(-120, 180), (-100, 180), (-100, 200)], '#0000ff', '#87cefa')
    square([(-100, 180), (-80, 180), (-80, 200)], '#87cefa', '#0000ff')

    square([(-200, 180), (-180, 180), (-180, 160)], '#87cefa', '#dbefff')
    square([(-180, 180), (-160, 180), (-160, 160)], '#0000ff', '#87cefa')
    square([(-160, 180), (-140, 180), (-140, 160)], '#87cefa', '#0000ff')
    square([(-140, 160), (-120, 160), (-120, 180)], '#0000ff', '#87cefa')
    square([(-120, 160), (-100, 160), (-100, 180)], '#87cefa', '#0000ff')
    square([(-100, 160), (-80, 160), (-80, 180)], '#dbefff', '#87cefa')

    square([(-200, 160), (-180, 160), (-180, 140)], '#dbefff', '#87cefa')
    square([(-180, 160), (-160, 160), (-160, 140)], '#87cefa', '#dbefff')
    square([(-160, 160), (-140, 160), (-140, 140)], '#0000ff', '#87cefa')
    square([(-140, 140), (-120, 140), (-120, 160)], '#87cefa', '#0000ff')
    square([(-120, 140), (-100, 140), (-100, 160)], '#dbefff', '#87cefa')
    square([(-100, 140), (-80, 140), (-80, 160)], '#87cefa', '#dbefff')

    square([(-200, 120), (-180, 120), (-180, 140)], '#dbefff', '#87cefa')
    square([(-180, 120), (-160, 120), (-160, 140)], '#87cefa', '#dbefff')
    square([(-160, 120), (-140, 120), (-140, 140)], '#0000ff', '#87cefa')
    square([(-140, 140), (-120, 140), (-120, 120)], '#87cefa', '#0000ff')
    square([(-120, 140), (-100, 140), (-100, 120)], '#dbefff', '#87cefa')
    square([(-100, 140), (-80, 140), (-80, 120)], '#87cefa', '#dbefff')

    square([(-200, 100), (-180, 100), (-180, 120)], '#87cefa', '#dbefff')
    square([(-180, 100), (-160, 100), (-160, 120)], '#0000ff', '#87cefa')
    square([(-160, 100), (-140, 100), (-140, 120)], '#87cefa', '#0000ff')
    square([(-140, 120), (-120, 120), (-120, 100)], '#0000ff', '#87cefa')
    square([(-120, 120), (-100, 120), (-100, 100)], '#87cefa', '#0000ff')
    square([(-100, 120), (-80, 120), (-80, 100)], '#dbefff', '#87cefa')

    square([(-200, 80), (-180, 80), (-180, 100)], '#0000ff', '#87cefa')
    square([(-180, 80), (-160, 80), (-160, 100)], '#87cefa', '#0000ff')
    square([(-160, 80), (-140, 80), (-140, 100)], '#dbefff', '#87cefa')
    square([(-140, 100), (-120, 100), (-120, 80)], '#87cefa', '#dbefff')
    square([(-120, 100), (-100, 100), (-100, 80)], '#0000ff', '#87cefa')
    square([(-100, 100), (-80, 100), (-80, 80)], '#87cefa', '#0000ff')
    turtle.done()

main()