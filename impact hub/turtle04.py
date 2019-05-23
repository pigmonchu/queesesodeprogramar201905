import turtle
mitortuga = turtle.Turtle()

figura = input("Quieres triangulo o cuadrado (T/C):")

if figura == 'T':
    for _ in range(3):
        mitortuga.forward(50)
        mitortuga.left(120)
        
        
if figura == 'C':
    for _ in range(4):
        mitortuga.forward(50)
        mitortuga.left(90)
        
turtle.mainloop()