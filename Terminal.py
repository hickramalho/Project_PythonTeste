import subprocess
subprocess.call("ls", shell=True)

arquivos_pasta = subprocess.run(["ls"], capture_output=True, text=True)

print (arquivos_pasta.stdout)


with open("teste.txt", "w") as arquivo:
    arquivo.write("Alguma coisa")

with open("teste.txt", "r")
