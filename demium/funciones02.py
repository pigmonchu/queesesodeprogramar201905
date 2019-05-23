import turtle
mitortuga = turtle.Turtle()

def poligono(num_lados):
    for _ in range(num_lados):
        mitortuga.forward(100)
        mitortuga.left(360/num_lados)
        

figura = input("Triángulo (T) o Cuadrado (C)")

if figura == 'T':
    for _ in range(10):
        poligono(3)
        mitortuga.left(36)
elif figura == 'C':
    poligono(4)
elif figura == 'P':
    poligono(5)
else:
    print("opción incorrecta")

