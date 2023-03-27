![cesarsquadslogosmall](https://user-images.githubusercontent.com/111138996/222937406-ceec455c-ab76-4edc-a618-96c7d752550d.png)

   * [Sobre o projeto](#-sobre-o-projeto)
   * [Instalação](#-instalação)
   * [Entrega 01](#-entrega-01)
   * [Entrega 02](#-entrega-02)
   * [Entrega 03](#-entrega-03)
   * [Entrega 04](#-entrega-04)
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

### ✅ Entrega 01

27/03

- Stories / Board / Backlog

**[Jira](https://projetofds.atlassian.net/)** 

![03-27-board-jira](https://user-images.githubusercontent.com/111138996/228053541-ba425351-bbc6-4d9d-90ea-6346bd3a9670.png)

![27-03-backlog-jira](https://user-images.githubusercontent.com/111138996/228053557-127208ce-e8ad-4e2d-87ac-5a955df22187.png)

- Protótipo Lo-Fi v1

[Figma](https://www.figma.com/proto/8MrwJKcy4XKxQdEP1Ywi44/Prototipo-Lo-fi?node-id=27-178&scaling=min-zoom&page-id=0%3A1&starting-point-node-id=27%3A178)

[Youtube](https://youtu.be/oxeSl30gNEc)

[![https://youtu.be/oxeSl30gNEc](https://img.youtube.com/vi/oxeSl30gNEc/0.jpg)](https://youtu.be/oxeSl30gNEc)

---

### 🔲 Entrega 02

17/04

- Diagrama de atividades do sistema
    Acessível através do README do projeto no Github
    
- Ambiente de versionamento atuante
    Com commits frequentes (no mínimo semanais)
    
- Issue/bug tracker atualizado (no GitHub)
    Enviar print da tela no dia da entrega
    
- Deploy de algumas histórias (mínimo 3)
    Aplicação em produção
    Enviar link e instruções de acesso
    Enviar screencast do uso do sistema (com áudio ou legenda)
    
- Programação em Par experimentada e usado
    Se não utilizado, com boa justificativa
    Relato acessível através do README do projeto no Github
    
- Quadro da Sprint 01 atualizado refletindo a entrega
    Enviar print do quadro da sprint

---

### 🔲 Entrega 03

15/05

- Seleção de mais histórias para implementar (pelo menos 3)
    Criação de nova sprint no JIRA
    
- Atualização dos protótipos de Lo-Fi
    Sketches e storyboards para as novas histórias
    Envio de novo screencast (ênfase nas novas histórias)
    
- Atualização do diagrama de atividades

- Ambiente de versionamento atuante
    Com commits frequentes (no mínimo semanais)
    
- Deploy das novas histórias
    Envio de novo screencast (ênfase nas novas histórias)
    
- Issue/bug tracker atualizado (no GitHub)
    Enviar print da tela no dia da entrega
    
- Testes de Sistema (E2E) Automatizados
    Enviar screencast da execução dos testes
    
- Atualização sobre o uso da programação em pares

- Quadro da Sprint 02 atualizado refletindo a entrega
    Enviar print do quadro da sprint

---

### 🔲 Entrega 04

12/06

- Seleção de mais histórias para implementar (pelo menos 3)
    Criação de nova sprint no JIRA
    
- Atualização dos protótipos de Lo-Fi
    Sketches e storyboards para as novas histórias
    Envio de novo screencast (ênfase nas novas histórias)
    
- Atualização do diagrama de atividades

- Ambiente de versionamento atuante
    Com commits frequentes (no mínimo semanais)
    
- Deploy das novas histórias
    Envio de novo screencast (ênfase nas novas histórias)
    
- Issue/bug tracker atualizado (no GitHub)
    Enviar print da tela no dia da entrega
    
- Testes de Sistema (E2E) Automatizados
    Enviar screencast da execução dos testes
    
- CI/CD com build e deployment automatizado
    Pipeline criada no Github
    Enviar screencast do processo de build e deployment
    
- Atualização sobre o uso da programação em pares

- Quadro da Sprint 03 atualizado refletindo a entrega
    Enviar print do quadro da sprint
    Documentação clara e objetiva conduzindo qualquer 
    pessoa a montar o ambiente corretamente e contribuir com o projeto (README)

---

### 🛠 Ferramentas

-   **[Jira](https://projetofds.atlassian.net/)** 
-   **[Django](https://www.djangoproject.com/)**
-   **[Visual Studio Code](https://code.visualstudio.com/)** 

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
