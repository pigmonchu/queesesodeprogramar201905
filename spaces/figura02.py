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


figura = input("Quieres un triángulo (T) o un cuadrado (C):")

if figura == 'C':
    cuadrado()
    mitortuga.forward(75)
    cuadrado()

elif figura == 'T':
    triangulo()
else:
    print("que no")
