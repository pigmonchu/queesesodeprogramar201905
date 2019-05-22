import turtle
mitortuga = turtle.Turtle()

def poligono_regular(num_lados, longitud_lado):
    for _ in range(num_lados):
        mitortuga.forward(longitud_lado)
        mitortuga.left(360/num_lados)
figura = input("Triangulo, Cuadrado o Pentagono (T, C, P)")

if figura == 'T':
    poligono_regular(3, 50)
elif figura == 'C':        
    poligono_regular(4, 50)
elif figura == 'P':
    poligono_regular(5, 50)
else:
    print("Nada que dibujar")