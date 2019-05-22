import turtle
mitortuga = turtle.Turtle()

figura = input("Quieres triangulo o cuadrado (T/C):")

def triangulo():
    for _ in range(3):
        mitortuga.forward(50)
        mitortuga.left(120)
def cuadrado():
    for _ in range(4):
        mitortuga.forward(50)
        mitortuga.left(90)

    
if figura == 'T':
    triangulo()
elif figura == 'C':        
    cuadrado()
else:
    print("Nada que dibujar")



