# Script em python que tira print a cada 3 segundos e envia para
# o site: https://transfer.sh

# by: Nano-9
# Github: https://github.com/nano-9

# pip install requests pyscreenshot

import os
import sys
import requests
import pyscreenshot
from time import sleep

local = r"\Users\Cliente\Downloads"

os.system("clear")

def salvar_screenshot_e_enviar():

	"""
	Essa função tira print da tela, salva na pasta (tela) dentro de
	Downloads no pc e envia o print da tela para o site https://transfer.sh
	que é um servidor online de salvamento de imagens
	"""

	nome_screenshot = 1

	while True:

		s = pyscreenshot.grab()
		os.chdir(str(local)+"\\tela")

		with open("tela","wb") as file:
			s.save("tela" + str(nome_screenshot) + ".png")
			file.close()

		for tela in os.listdir(str(local)+"\\tela"):

			if tela.endswith(".png"):
				with open(tela,"rb") as file:
					r = requests.post("https://transfer.sh",files={tela: file})
					if r.status_code == 200:
						print("link: {}".format(r.text))
						nome_screenshot+=1
			else:
				os.remove(tela)
				
		sleep(3)


def criar_pasta():

	check = 0
	"""
	Essa função verifica se tem alguma pasta chamada tela na área de Downloads,
	caso não tenha nenhuma pasta com esse nome, ela irá criar uma pasta chamada tela
	"""
	while check == 0:

		for x in os.listdir(str(local)):
			if x == "tela":
				check = 1
				salvar_screenshot_e_enviar()
			else:
				os.chdir(local)
				os.makedirs("tela",exist_ok=True)

if __name__ == "__main__":
	criar_pasta()

# End
