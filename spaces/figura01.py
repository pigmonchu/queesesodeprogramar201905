import turtle

mitortuga = turtle.Turtle()

figura = input("Quieres un triángulo (T) o un cuadrado (C):")

if figura == 'C':
    for v in range(4):
        mitortuga.forward(50)
        mitortuga.left(90)

elif figura == 'T':
    for v in range(3):
        mitortuga.forward(50)
        mitortuga.left(120)
else:
    print("que no")