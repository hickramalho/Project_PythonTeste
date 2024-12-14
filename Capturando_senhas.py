import subprocess
import os
import sys
wifi_nomes = []
wifi_senhas = []
wifi_arquivos = []

comando = subprocess.run (["netsh", 'wlan', 'export', 'profile', 'key=clear'], capture_output=True).stdout

pasta_atual = os.getcwd()

for arquivo in os.listdir(pasta_atual):
    if arquivo.startswith("Wi-Fi") and arquivo.endswith(".xml"):
        wifi_arquivos.append(arquivo)
    
for novo_arquivo_atual in wifi_arquivos:

 with open(arquivo_atual, "r") as a:
    for linha in a.readlines():
        if "name" in linha and not nome_encontrado:
            sem_espaco = linha.strip()
            novo_texto = sem_espaco[6:]
            texto_limpo = novo_texto [:-7]
            wifi_nomes.append(linha)
        if "keyMaterial" in linha:
            sem_espaco = linha.strip()
            novo_texto = sem_espaco[13:]
            texto_limpo = novo_texto [:-14]
            wifi_nomes.append(linha)
for nome, senha, in zip(wifi_nomes, wifi_senhas):
    sys.stdout = open("wifi.txt", "a")
    print("Nome da rede: ", nome, "Senha: ", senha)
    sys.stdout.close()