import turtle

mitortuga = turtle.Turtle()

def cuadrado():
    for v in range(4):
        mitortuga.forward(50)
        mitortuga.left(90)
        
def triangulo():
    for v in range(3):
        mitortuga.forward(50)
        mitortuga.left(120)


for i in range(36):
    cuadrado()
    mitortuga.left(10)
