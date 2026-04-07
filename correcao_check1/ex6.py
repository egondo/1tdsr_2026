x = float(input("X: "))
y = float(input("Y: "))


if x == 0 and y == 0:
    print("ORIGEM")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
elif x > 0 and y > 0:
    print("Quadrante 1")
elif y > 0 and x < 0:
    print("Quadrante 2")
elif y < 0 and x < 0:
    print("Quadrante 3")
else:
    print("Quadrante 4")
