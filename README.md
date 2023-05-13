![cesarsquadslogosmall](https://user-images.githubusercontent.com/111138996/222937406-ceec455c-ab76-4edc-a618-96c7d752550d.png)

  - [.](#)
  - [🤖 Instalação](#-instalação)
  - [✅ Entrega 01](#-entrega-01)
  - [✅ Entrega 02](#-entrega-02)
  - [✅ Entrega 03](#-entrega-03)
  - [🔲 Entrega 04](#-entrega-04)
  - [🛠 Ferramentas](#-ferramentas)
  - [👨‍💻 Contribuidores](#-contribuidores)


### 💻 Sobre o projeto

**cesar.squads** é um App de criação e visualização rápida de grupos no formato *squads*.

Aplicação Web com design adaptável, desenvolvido em Python com Django e Banco de Dados usando Sqlite.

Usa como referência o [Modelo Spotify](https://www.atlassian.com/agile/agile-at-scale/spotify) de organização de trabalho em times ágeis:
    
![squadfw](https://user-images.githubusercontent.com/111138996/222938051-d1dce37f-c48f-4710-b6eb-42eb2693c22b.png)

Projeto da disciplina de **Fundamentos de Desenvolvimento de Software** da graduação em **Ciência da Computação** da [CESAR School](https://www.cesar.school/).
  
  
.
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
Instalar dependencias no venv:
```
pip install -r requirements.txt
```
<sub>*A extensão *Django* ajuda na sintaxe e snippets.</sub>

Criar banco de dados:
```
python manage.py migrate
```
<sub>*A extensão *SQLite* e *SQLite Viewer* permitem visualizar o banco de dados.</sub>

Instalar requirements:
```
pip install -r requirements.txt
```
Criar superuser:
```
python manage.py createsuperuser
```
Rodar servidor:
```
python manage.py runserver
```
<sub>*link de acesso ao preview *'/admin' -> dashboard 
*ctrl+c stop no servidor</sub>


---

### ✅ Entrega 01

27/03

- Stories / Board / Backlog

**[Jira](https://projetofds.atlassian.net/jira/software/projects/SQUAD/boards/2/backlog)** 

![03-27-board-jira](https://user-images.githubusercontent.com/111138996/228053541-ba425351-bbc6-4d9d-90ea-6346bd3a9670.png)

![27-03-backlog-jira](https://user-images.githubusercontent.com/111138996/228053557-127208ce-e8ad-4e2d-87ac-5a955df22187.png)

- Protótipo Lo-Fi v1

[Figma](https://www.figma.com/proto/8MrwJKcy4XKxQdEP1Ywi44/Prototipo-Lo-fi?node-id=27-178&scaling=min-zoom&page-id=0%3A1&starting-point-node-id=27%3A178)

- Screencast Protótipo

[Youtube](https://youtu.be/oxeSl30gNEc)

[![https://youtu.be/oxeSl30gNEc](https://img.youtube.com/vi/oxeSl30gNEc/0.jpg)](https://youtu.be/oxeSl30gNEc)

---

### ✅ Entrega 02

17/04

  
  - Acesso ao App em produção:
    http://cesarsquads-env.eba-3ghckqxt.us-east-2.elasticbeanstalk.com/
    
    Instruções:
    ```
    Ao acessar o link acima:
    - Clicar em 'Entrar' ou 'Cadastrar'
      - Entrar com usuário 'teste' 'senha1234'
      - (ou) Cadastrar novo usuário e entrar.
    - Na página do Perfil, digitar no campo 'Nome da Tribo' e clicar em 'Criar'
    - Na página da Tribo, digitar no campo 'Nome da Squad' e clicar em 'Criar'   
    
    ```
   - Screencast:

  [Youtube](https://youtu.be/tzg8IfKUan8)

  [![https://youtu.be/tzg8IfKUan8](https://img.youtube.com/vi/tzg8IfKUan8/0.jpg)](https://youtu.be/tzg8IfKUan8)
  
  - 3 histórias do sprint backlog na coluna **Done**
   **[Jira](https://projetofds.atlassian.net/jira/software/projects/SQUAD/boards/2/backlog)** 
   
   ![cesarsquad-jiraprint-sprint1](https://user-images.githubusercontent.com/111138996/232496019-c01cfe48-b09b-4c61-87ec-0c3a7bddc377.png)

  - Diagrama de atividades do sistema
  
   ![cesarsquad drawio](https://user-images.githubusercontent.com/111138996/232489312-24a2851d-b89d-4da2-a936-ceea9d2e29a9.png)

  -  Issue/bug tracker no dia 17/04

   ![cesarsquads_issues-bug-tracker17-04](https://user-images.githubusercontent.com/111138996/232498226-cc1a8375-bad9-43f5-bc3e-d012b007abc7.png)

  - Nosso relato sobre a utilização de pair programming:

    Foi nossa primeira vez trabalhando com pair programming em um grupo de 6 pessoas, mas foi uma experiência interessante. Nossas duplas eram alternadas, porque nem sempre os mesmos integrantes estavam disponíveis para produzir alguma tarefa e, assim, tivemos a oportunidade de trabalhar com diferentes colegas de equipe e trocar conhecimentos.

    Uma das principais vantagens desse modelo que seguimos foi conseguirmos aprender muito mais sobre o Django. Trabalhando com diferentes pessoas, fomos capazes de ver abordagens diferentes para resolver os problemas, aprender novas técnicas de programação e aprimorar nossa capacidade de trabalhar em equipe.

    No entanto, também houveram alguns desafios em trabalhar em grupo dessa maneira. Como as duplas eram alternadas, às vezes precisávamos explicar para o novo parceiro(a) onde estávamos no projeto, o que já tínhamos feito e o que precisava ser feito. Isso foi um pouco cansativo e consumiu algum tempo, mas no final, todos nós conseguimos nos comunicar bem e trabalhar juntos de maneira eficaz.

    No geral, trabalhar em grupo dessa maneira foi uma experiência positiva e produtiva. Embora tenha havido alguns desafios, as vantagens superaram as dificuldades. Foi uma ótima maneira de aprender mais sobre o Django e trabalhar em equipe de forma colaborativa.

---

### ✅ Entrega 03

15/05
   
- Atualização dos protótipos de Lo-Fi WIP
    Sketches e storyboards para as novas histórias
    Envio de novo screencast (ênfase nas novas histórias)
    
- Diagrama de atividades do sistema
![cesarsquad](https://github.com/pedro-coelho-dr/fdsproject/assets/111138996/834f0a6a-d3bf-4936-9bde-18a7d5b6e5c3)

- Deploy das novas histórias WIP
    Envio de novo screencast (ênfase nas novas histórias)
    
- Issue/bug tracker atualizado (no GitHub) WIP
    Enviar print da tela no dia da entrega
    
- Testes de Sistema (E2E) Automatizados WIP
    Enviar screencast da execução dos testes
    
- Atualização sobre o uso da programação em pares WIP

- Quadro da Sprint 02 atualizado refletindo a entrega WIP
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

-   **[Django](https://www.djangoproject.com/)**
-   **[Jira](https://projetofds.atlassian.net/jira/software/projects/SQUAD/boards/2/backlog)** 
-   **[AWS Elastic Beanstalker](https://aws.amazon.com/elasticbeanstalk/)** 
-   **[Figma](https://www.figma.com/)**
-   **[Diagrams.net](https://app.diagrams.net/)**
-   **[Django Bootstrap](https://django-bootstrap-v5.readthedocs.io/en/latest/)**
-   **[SQLite](https://sqlite.org/)**
-   **[Python](https://www.python.org/)**
-   **[Virtualenv](https://virtualenv.pypa.io/)**
-   **[Github](https://github.com/)**
-   **[Visual Studio Code](https://code.visualstudio.com/)**
-   **[Selenium](https://www.selenium.dev/)**
-   **[Pillow](https://pypi.org/project/Pillow/)**
-   **[Bootstrap](https://getbootstrap.com/)**
-   **[Selenium](https://www.selenium.dev/)**

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
