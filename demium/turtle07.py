import turtle
mitortuga = turtle.Turtle()


figura = input("Triángulo (T) o Cuadrado (C)")

if figura == 'T':
    for _ in range(3):
        mitortuga.forward(100)
        mitortuga.left(120)
elif figura == 'C':
    for _ in range(4):
        mitortuga.forward(100)
        mitortuga.left(90)
elif figura == 'P':
    for _ in range(5):
        mitortuga.forward(100)
        mitortuga.left(72)
else:
    print("opción incorrecta")
