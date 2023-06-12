![cesarsquadslogosmall](https://user-images.githubusercontent.com/111138996/222937406-ceec455c-ab76-4edc-a618-96c7d752550d.png)

  - [.](#)
  - [🤖 Instalação](#-instalação)
  - [✅ Entrega 01](#-entrega-01)
  - [✅ Entrega 02](#-entrega-02)
  - [✅ Entrega 03](#-entrega-03)
  - [✅ Entrega 04](#-entrega-04)
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
    CesarSquads-env.eba-hqizgypw.us-east-2.elasticbeanstalk.com
    
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
  
  - Acesso ao App em produção:
    CesarSquads-env.eba-hqizgypw.us-east-2.elasticbeanstalk.com
    
    Instruções:
    ```
    Ao acessar o link acima:
    - Clicar em 'Entrar' ou 'Cadastrar'
      - Entrar com usuário 'teste' 'senha1234'
      - (ou) Cadastrar novo usuário e entrar.
    - Na página do Perfil é possível:
      - Acessar tribos que faz parte.
      - Pesquisar tribos
      - Criar tribo  
    - Na página da Tribo:
      -  Alterar avatar da tribo
      -  Alterar descrição da tribo
      -  Criar squad
      -  Participar de squad
    - Na página da Squad:
      -  Alterar avatar da squad
      -  Editar descrição da squad
    
    ```

 - Deploy:
    [Youtube](https://youtu.be/DUQ1nYiun9o)

    [![https://youtu.be/DUQ1nYiun9o](https://img.youtube.com/vi/DUQ1nYiun9o/0.jpg)](https://youtu.be/DUQ1nYiun9o)
  
 - Teste de Sistema:
    [Youtube](https://youtu.be/pONzDeGGR9A)

    [![https://youtu.be/pONzDeGGR9A](https://img.youtube.com/vi/pONzDeGGR9A/0.jpg)](https://youtu.be/pONzDeGGR9A)
  
 - Protótipo Lo-fi: 
     [Youtube](https://youtu.be/Yx6NKMHzndc)

    [![https://youtu.be/Yx6NKMHzndc](https://img.youtube.com/vi/Yx6NKMHzndc/0.jpg)](https://youtu.be/Yx6NKMHzndc)
  
  [FIGMA](https://www.figma.com/file/8MrwJKcy4XKxQdEP1Ywi44/Prototipo-Lo-fi?type=design&node-id=0%3A1&t=c8ICu2C5opbhbi4f-1)
    
- Diagrama de atividades do sistema

![cesarsquad](https://github.com/pedro-coelho-dr/fdsproject/assets/111138996/834f0a6a-d3bf-4936-9bde-18a7d5b6e5c3)

- Quadro da Sprint:

![quadro_entrega3](https://github.com/pedro-coelho-dr/fdsproject/assets/111138996/f9f1c1d3-3bc6-4c2d-bcae-1320f922f9a0)

  **[Jira](https://projetofds.atlassian.net/jira/software/projects/SQUAD/boards/2/backlog)** 

- Issue/bug tracker:

 ![github_issues_bug_tracker_entrega3](https://github.com/pedro-coelho-dr/fdsproject/assets/111138996/2aaca34f-f71c-4167-942e-53aa4bc6f277)

    
- Atualização sobre o uso da programação em pares:
   	Realizamos mais uma sprint trabalhando com pair programming e agora, optamos por ter pares fixos, onde cada dupla ficou responsável por uma história específica do projeto. Além disso, introduzimos uma nova ferramenta, a extensão Live Share, que facilitou a troca entre as funções dos pares.

	Essas mudanças trouxeram benefícios excelentes para a nossa equipe. Ao optar pelos pares fixos, conseguimos desenvolver um entendimento mais profundo das histórias que estávamos trabalhando, e isso permitiu cada dupla tornar-se 'especialista' na sua história, o que resultou em uma maior produtividade e melhor qualidade do código produzido.

	A utilização da extensão Live Share também foi um passo importante. Com essa ferramenta, pudemos compartilhar facilmente nossos ambientes de desenvolvimento, permitindo que os pares trabalhassem em conjunto de maneira mais fluida. Foi possível alternar entre as funções de piloto e copiloto, possibilitando que ambos os membros da dupla contribuíssem efetivamente no processo de codificação. Embora ainda tenhamos enfrentado alguns desafios de comunicação e coordenação entre as duplas, eles foram minimizados em comparação a abordagem anterior de pares alternados. 

	No geral, essa nova forma de trabalhar em grupo através do pair programming, com pares fixos e a utilização da extensão Live Share, mostrou-se mais produtiva e eficiente. Essa experiência desenvolveu mais a nossa habilidade de colaboração e nos aproximou dos objetivos finais do projeto.

---

### ✅ Entrega 04

12/06

  - Acesso ao App em produção:
    [CesarSquads-env.eba-hqizgypw.us-east-2.elasticbeanstalk.com](CesarSquads-env.eba-hqizgypw.us-east-2.elasticbeanstalk.com)
    
    Instruções:
    ```
    Ao acessar o link acima:
    - Clicar em 'Entrar' ou 'Cadastrar'
      - Entrar com usuário 'teste' 'senha1234'
      - (ou) Cadastrar novo usuário e entrar.
    - Na página do Perfil é possível:
      - Acessar tribos que faz parte.
      - Pesquisar tribos
      - Criar tribo
    - Na página da Tribo:
      -  Alterar avatar da tribo
      -  Alterar descrição da tribo
      -  Criar squad
      -  Participar de squad
      -  Remover usuario da tribo
      -  Sair da tribo
    - Na página da Squad:
      -  Alterar avatar da squad
      -  Editar descrição da squad
      -  Remover usuario da squad
      -  Sair da Squad
    
    ```
   
- Deploy
    [Youtube](https://youtu.be/eoy0nFL6FWU)

    [![https://youtu.be/eoy0nFL6FWU](https://img.youtube.com/vi/eoy0nFL6FWU/0.jpg)](https://youtu.be/eoy0nFL6FWU)
    
    
- Testes de Sistema (E2E) Automatizados
    [Youtube](https://youtu.be/n8R2FJ7mQjU)

    [![https://youtu.be/n8R2FJ7mQjU](https://img.youtube.com/vi/n8R2FJ7mQjU/0.jpg)](https://youtu.be/n8R2FJ7mQjU)
    
- CI/CD com build e deployment automatizado
    [Youtube](https://youtu.be/1DHMIDcagV8)

    [![https://youtu.be/1DHMIDcagV8](https://img.youtube.com/vi/1DHMIDcagV8/0.jpg)](https://youtu.be/1DHMIDcagV8)
    
- Protótipo Lo-fi: 
    [Youtube](https://youtu.be/AC1qABSSOCs)

    [![https://youtu.be/AC1qABSSOCs](https://img.youtube.com/vi/AC1qABSSOCs/0.jpg)](https://youtu.be/AC1qABSSOCs)
  
 [FIGMA](https://www.figma.com/file/8MrwJKcy4XKxQdEP1Ywi44/Prototipo-Lo-fi?type=design&node-id=0%3A1&t=c8ICu2C5opbhbi4f-1)
 
- Diagrama de atividades do sistema

![Diagrama sem nome (1)](https://github.com/pedro-coelho-dr/fdsproject/assets/111138996/6ab701d1-b948-4c64-ab82-f371b9475530)

    
- Quadro da Sprint:
![print_jira](https://github.com/pedro-coelho-dr/fdsproject/assets/111138996/00fc9acb-c26b-4218-8608-550098ac10bd)

  **[Jira](https://projetofds.atlassian.net/jira/software/projects/SQUAD/boards/2/backlog)** 

- Issue/bug tracker:
![print_issuesbuggithub](https://github.com/pedro-coelho-dr/fdsproject/assets/111138996/ccb815bc-8bd1-4741-83ed-c8f1a2740d57)
    
- Atualização sobre o uso da programação em pares:
	Para a entrega 04, continuamos a realizar sprints e adotando o modelo de pares fixos para o pair programming. Além disso, a extensão Live Share mostrou-se MUITO essencial para a conclusão das nossas entregas.

	O pair programming com pares fixos e o uso da extensão Live Share trouxeram benefícios notáveis para nosso grupo. Essa abordagem foi essencial para alcançarmos os objetivos finais do projeto, fortalecendo nossa capacidade de trabalho em equipe. O pair programming se mostrou uma prática valiosa para o desenvolvimento ágil e aprimorou nossas habilidades.
	
- Apresentação final
	
	[Cesar Squads.pdf](https://github.com/pedro-coelho-dr/fdsproject/files/11724260/Cesar.Squads.pdf)
	
	[Canvas](https://www.canva.com/design/DAFliAkrGAo/SaFM9pRV7rXyTO0mcEokfw/view?utm_content=DAFliAkrGAo&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)


---

### 🛠 Ferramentas

-   **[Django](https://www.djangoproject.com/)**
-   **[Jira](https://projetofds.atlassian.net/jira/software/projects/SQUAD/boards/2/backlog)** 
-   **[AWS Elastic Beanstalker](https://aws.amazon.com/elasticbeanstalk/)** 
-   **[Figma](https://www.figma.com/)**
-   **[Diagrams.net](https://app.diagrams.net/)**
-   **[Bootstrap](https://getbootstrap.com/)**
-   **[Pillow](https://pypi.org/project/Pillow/)**
-   **[SQLite](https://sqlite.org/)**
-   **[Python](https://www.python.org/)**
-   **[Virtualenv](https://virtualenv.pypa.io/)**
-   **[Selenium](https://www.selenium.dev/)**
-   **[Github](https://github.com/)**
-   **[LiveShare](https://visualstudio.microsoft.com/pt-br/services/live-share/)**
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
