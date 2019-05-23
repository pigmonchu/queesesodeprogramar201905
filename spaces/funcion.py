import turtle

mitortuga = turtle.Turtle()


def poligono(longitud_lado, num_lados):
    for v in range(num_lados):
        mitortuga.forward(longitud_lado)
        mitortuga.left(360/num_lados)
    


poligono(50, 3)
poligono(100,3)
poligono(100, 5)