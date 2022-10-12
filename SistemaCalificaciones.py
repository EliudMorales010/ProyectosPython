valor = int(input("Digite un valor entre 0 - 10:"))
if 9 <= valor <= 10:
    print("A")
elif 8 <= valor < 9:
    print("B")
elif 7 <= valor < 8:
    print("C")
elif 6 <= valor < 7:
    print("D")
elif 0 <= valor < 6:
    print("F")
else:
    print("Valor incorrecto! Verifique")