# Descripcion: Paint usando Turtle para dibujar 
# Autores: Armando Vasquez Ambrocio | A01669283
#          Diana Karen Barrales Victorio | A018022299
# Fecha de modificacion: 30/10/2025

# Importacion de API Tutle y vector para dibujo 2D
from turtle import *

from freegames import vector

# Dibuja una linea desde el punto start al punto end
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

# Dibuja un cuadrado tomando como referencia start y el end como un desplazamiento horizontal
def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

# Dibuja un circulo con centro en start y se calcula el radio haciendo uso de start y end
def circle(start, end):
    """Draw circle from start to end."""
    import turtle as t

    r = ((end.x -start.x)**2 + (end.y - start.y)**2) ** 0.5
    if r == 0:
        return

    up()
    goto(start.x, start.y)

    setheading(0)
    up(); forward(r); left(90); down()

    begin_fill()
    t.circle(r)
    end_fill()

    up()
    right(90); backward(r)

# Dibuja un rectangulo con esquina en start y esquina opuesta en end
def rectangle(start, end):
    """Draw rectangle form start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()
    up()

# Dibuja un triangulo equilatero con esquina en start y end define el tamaño de uno de sus lados
def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()
    up()

# Maneja los clicls. El primer clic se guarda como start y el segundo clic dibuja la figura seleccionada.
def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

# Guarda un valor para una clave indicada
def store(key, value):
    """Store value in state at key."""
    state[key] = value

# Estado global
state = {'start': None, 'shape': line}

# Configuracion de la ventana
setup(420, 420, 370, 0)

# Captura de clics
onscreenclick(tap)
listen()

# Deshacer ultima accion
onkey(undo, 'u')

# Colores y figuras permitidas en el programa
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('pink'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
