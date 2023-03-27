![cesarsquadslogosmall](https://user-images.githubusercontent.com/111138996/222937406-ceec455c-ab76-4edc-a618-96c7d752550d.png)

   * [Sobre o projeto](#-sobre-o-projeto)
   * [Instalação](#-instalação)
   * [Ferramentas](#-ferramentas)
   * [Contribuidores](#-contribuidores)


### 💻 Sobre o projeto

**cesar.squads** é um App de criação e visualização rápida de grupos no formato *squads*.

Aplicação Web com design adaptável, desenvolvido em Python com Django e Banco de Dados usando Sqlite.

Usa como referência o [Modelo Spotify](https://www.atlassian.com/agile/agile-at-scale/spotify) de organização de trabalho em times ágeis:
    
![squadfw](https://user-images.githubusercontent.com/111138996/222938051-d1dce37f-c48f-4710-b6eb-42eb2693c22b.png)

Projeto da disciplina de **Fundamentos de Desenvolvimento de Software** da graduação em **Ciência da Computação** da [CESAR School](https://www.cesar.school/).
  
  
---


### 🤖 Instalação

Após clonar o repositório no seu diretório local: 

  
Instalar o ambiente virtual:
```
pip install virtualenv
```
Criar o ambiente virtual:
```
virtualenv venv
```
Ativar ambiente virtual:
```
source venv/Scripts/activate
```

<sub>*(venv) aparece no terminal</sub>


Desativar ambiente virtual:
```
deactivate
```
Instalar django no venv:
```
pip install django
```
Criar banco de dados:
```
python manage.py migrate
```
Rodar servidor:
```
python manage.py runserver
```
<sub>*link de acesso ao preview  
*ctrl+c stop no servidor</sub>


Criar superuser:
```
python manage.py createsuperuser
```
<sub>username=~~****~~  
email=~~****@cesar.school~~  
password=~~******~~</sub>  

As pastas devem ficar assim:  
![image](https://user-images.githubusercontent.com/111138996/223016134-0659262e-d8ef-478f-a7a6-803d073a4aa7.png)  
<sub>*A extensão *SQLite Viewer* permite visualizar o banco de dados.</sub>
<sub>*A extensão *Django* ajuda na sintaxe e snippets.</sub>  


---

### 🛠 Ferramentas

-   **[Jira](https://projetofds.atlassian.net/)** 
-   **[Django](https://www.djangoproject.com/)**
-   **[Visual Studio Code](https://code.visualstudio.com/)**
-   **[Figma](https://www.figma.com/)**  →  **[Protótipo (CESAR Squads)](https://www.figma.com/proto/8MrwJKcy4XKxQdEP1Ywi44/Prototipo-Lo-fi?node-id=27-178&scaling=min-zoom&page-id=0%3A1&starting-point-node-id=27%3A178)**

---

### 👨‍💻 Contribuidores

<table>
  <tr>
    <td align="center"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/112348748?v=4" width="100px;" alt=""/><br /><sub><b>David Cândido</b></sub></a><br /></a></td>
    <td align="center"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/39159963?v=4" width="100px;" alt=""/><br /><sub><b>Francisco Luz</b></sub></a><br /></a></td>
        <td align="center"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/116602650?v=4" width="100px;" alt=""/><br /><sub><b>Gislaine Reis</b></sub></a><br /></a></td>
    <td align="center"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/116669790?v=4" width="100px;" alt=""/><br /><sub><b>Lucas Cortez</b></sub></a><br /></a></td>
    <td align="center"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/111138996?v=4" width="100px;" alt=""/><br /><sub><b>Pedro Coelho</b></sub></a><br /></a></td>
    <td align="center"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/112591325?v=4" width="100px;" alt=""/><br /><sub><b>Thiago Araújo</b></sub></a><br /></a></td>


    
    
    
  </tr>
</table>
