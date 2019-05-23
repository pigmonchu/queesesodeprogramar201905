import turtle
mitortuga = turtle.Turtle()

def triangulo():
    for _ in range(3):
        mitortuga.forward(100)
        mitortuga.left(120)

def cuadrado():
    for _ in range(4):
        mitortuga.forward(100)
        mitortuga.left(90)
        
def pentagono():
    for _ in range(5):
        mitortuga.forward(100)
        mitortuga.left(72)


figura = input("Triángulo (T) o Cuadrado (C)")

if figura == 'T':
    triangulo() 
elif figura == 'C':
    cuadrado()
elif figura == 'P':
    pentagono()
else:
    print("opción incorrecta")
