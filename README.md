# Sobre o spy_screen:

Ele é um script que monitora o usuário, tirando print a cada 3 segundos da tela
e fazendo upload do screenshot no site https://transfer.sh através de uma requisição post.

# Armazenamento das imagens:

Ele cria uma pasta chamada (tela) no diretório de downloads e usa essa pasta para armazenar os prints

# Objetivos do spy_screen:

[1] - Tirar um print da tela a cada 3 segundos e salvar
na pasta tela

[2] - Fazer uma requisição tipo post no site https://transfer.sh
e fazer upload da imagem

[3] - Retornar o link da imagem já postada no site

# Junção?

Esse meu código está aberto para quem quiser fazer um upgrade ou integrá-lo em algum outro script.
Irei fazer melhorias nele também!

# Para utilizar:

Digite: pip install -r requirements.txt
