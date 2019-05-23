import turtle
mitortuga = turtle.Turtle()

def estrella(num_lados,tamanno):
    for _ in range(num_lados):
        mitortuga.forward(tamanno)
        mitortuga.left(720/num_lados)
        
mitortuga.left(180)
estrella(5,100)
mitortuga.pu()
mitortuga.forward(200)
mitortuga.pd()
estrella(5,50)