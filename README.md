# _**Mercado da Bala**_

o projeto consiste em um desenvolvimento _Full Stack_ com o intuíto de ser um portal para fans de _Counter Strike 2_ ficarem por dentro das transferências mais atuais do cenário.

Foi criado um servidor Python-Django para realizar a extração das informações do site [Hltv.org](https://www.hltv.org/transfers) através de _Web Scrapping_, o servidor disponibiliza uma API 
para o Front-End puxar os dados.

O desenvolvimento do site foi feito com o framework Vue.js com o conceito de componentes e reatividade

Tecnologias utilizadas:

- Django -> servidor web
- Django REST Framework -> API Rest
- BS4 + Request -> Web Scrapping
- Vue.js + TypeScript -> desenvolvimento da página web e consumo da API
- PostgreSQL -> Banco de Dados

---

### Como Utilizar ? 

OBS: estou levando em conta que já tenha o Python e o Node instalado na máquina

Faça um `git clone` do repositório para a sua máquina

obs: o repositório já vem tanto com a página e o servidor, a API individual está disponibilizada neste [repositório]()

Você precisará configurar o servidor, realizando as seguintes etapas:
1.  Crie um ambiente virtual e instale as dependencias do projeto que estão no arquivos _requirements.txt_. Use o `pip` para isso: `pip install -r requirements.txt`
2.  Configure seu banco de dados. Como criei um BD personalizado a partir do PostgreSQL, você precisará fazer a mesma coisa. Quando criado você precisará alterar as configurações do Django de banco de dados:
   ```
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql", #caso seja outro banco de dados, consulte a documentação do Django
        "NAME": "nome do BD",
        "USER": "usuario",
        "PASSWORD": "senha",  
        "HOST": "host",
        "PORT": "porta"
    }
}
   ```
3.  Após configurado, realize os comandos:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Com tudo configurado corretamente basta rodar o servidor do projeto com `python manage.py runserver`
5. Para rodar o projeto Vue.js basta rodar o comando `npm run dev` 
