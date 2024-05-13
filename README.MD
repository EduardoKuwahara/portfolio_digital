# Portfólio digital de Eduardo Kuwahara Junior
## Orientador: Fabrício Galende Marques de Carvalho

<p align=center>
    <img src="mgt/EduK.jpg" alt="Eduardo Kuwahara" width="50%"></img>
</p>

## Tecnologias utilizadas:

- Git/Github
- HTML
- Markdown
- Flask
- Python
- CSS
- Bootstrap

# Como rodar a aplicação:
## O que será necessário

1. [Git](https://git-scm.com/downloads): Git para clonar o nosso repositório.

2. [Python](https://www.python.org/downloads/): Para rodar de maneira adequada a aplicação.

## 1º Passo: Clonando o repositório

<details>
  <summary><b>Clique aqui</b></summary>

  Siga os passo a seguir para clonar o repositório e rodar a aplicação.

  1. Crie uma pasta onde você deseja armazenar e clonar o repostório.
  2. Abra a pasta, clique no campo de exibição dos diretótio e digite o comando "cmd". (Ex: Área de Trabalho > Pasta do Repositório > ...)

  > _Obs.: Caso você esteja no LINUX, a parte de escrever "cmd" não irá funcionar, então clique com o botão direito na pasta que você criou e selecione a opção "Abrir no terminal"_

  O terminal irá abri e basta digitar o seguinte comando nele:

  ```
  git clone https://github.com/EduardoKuwahara/portfolio_digital.git

  ```
</details>
<br>

## Preparando ambiente da aplicação

<details>
  <summary><b>Clique aqui</b></summary>

  1. Acesse o terminal desta pasta que foi clonada, repetindo as intruções acima.

   ```
  utilize o comando "cd api" para entrar na pasta e dar os comandos:
  python -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

> _Caso você esteja em LINUX, digite os comandos desta maneira:_<br>
`python3 -m venv venv`<br>
`source venv/bin/activate`<br>
`pip install -r requirements.txt` (lembre-se de dar "cd api" para entrar na pasta e dar o comando)

</details>
<br>

## Iniciando e acessando a aplicação:

<details>
  <summary><b>Clique aqui</b></summary>

  1. Dentro do ambiente virtual e dentro da pasta api, execute o comando:
  ```
  flask run
  ```

  2. Entre no link que aparecerá no cmd copiando e colando ele no seu navegador.

  3. Após finalizar o uso do portifolio e para sair do ambiente virtual, no terminal, execute o atalho `Ctrl+C` para finalizar o serviço do Flask, e então execute o seguinte comando:
  ```
  deactivate
  ```

</details>




Validação Orientador. Fabrício Galende Marques de Carvalho 2024/01
