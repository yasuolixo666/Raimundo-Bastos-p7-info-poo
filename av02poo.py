frases_letra = [
    "Anota a placa é o trem",
    "Lili pros amigo que tão privado",
    "Se ela quer so fe so fe",
    "O dia ta lindo clima ensolarado",
    "lave o rosto nas aguas sagradas da pía",
    "nada com um dia apos o outro dia"
]

for frase in frases_letra:
    msg = ""
    bigger_len = ""
    i = 0
    a = frase.split(" ")

    while i < len(a):
        msg += str(len(a[i])) + "-"
        if len(a[i]) > len(bigger_len):
            bigger_len = a[i]

        i += 1

    msg = msg[-len(msg):-1]
    print("{:25s} {}".format(msg, bigger_len))