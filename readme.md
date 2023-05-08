#  Voxel-TI Desafio Back End
Talvez eu esteja exagerando um pouco, já que isso é só um teste para estágio, mas eu quero mostrar como eu enxergo a solução de softwares no geral.

## Arquitetura Limpa
Apesar de eu estar usando arquitetura limpa aqui, com inversão de dependência e outras coisas, sendo uma aplicação pequena e de apenas demonstrações, não era realmente necessário. Mas uma aplicação tipica de web, que tem muitos paralelos com a realide e intrisicamente ligado com casos de usos, bem como escrever e pegar dados de um banco de dados, a arquitetura limpa se mostra muito eficiente na manutenção no longo prazo, e creio ser ideal para grande parte das aplicações web.

## Banco de dados
Utilizei o banco de dados sqlite3, popular principalmente para ambientes de testes e coisas assim, não muito adequado para software em produção, Dependendo da aplicação, poderia ser um noSQL como um mongoDB ou um dos SGBD sql já populares, como o mySQL e o postgreSQL, mas como é só um teste, decidi usar esse pela facilidade.

## Nomeclaturas
### Domain/Repositories
Nesse caminho fica as definições de interface do projeto.
### Domain/Entity
Nesse caminho fica as entidades do projeto
### application/use_cases
Nesse caminho fica os casos de uso, que usa as definições de interface do projeto como argumento.
### infraestructure/
Nesse caminho fica a implementação que implementa as interfaces do projeto

### Inversão de dependência
Note que eu posso criar outra infraestrutura e continuar usando os mesmos casos de uso, eu posso inicialmente utilizar a infraestrutura de um banco de dados sqlite, como to utilizando inicialmente, posteriormente criar um para postgreSQL, mudando apenas a infraestrutura e passando como argumento pro caso de uso, assim a manutenção da aplicação fica bem mais tranquilo, não dependemos diretamente de uma tecnologia e ficamos preso a ela, na verdade, temos a liberdade de trocar assim que for necessário.


## Instruções
- Vá para a pasta root do projeto, onde há o arquivo "main.py"
- execute - ```pip install -r requirements.txt```
- A versão do python usada foi o 3.11.3, não acredito que irá ter algum problema caso seja executado em outra versão do python3, mas deixando aqui só por garantia
- baixa a extensão "SQLite Viewer" no visual studio code, para conseguir visualizar o banco de dados, ou busque a visualização de outra forma
- Execute python main.py
- O código será executado no terminal, e, além disso, irá criar um arquivo "product.db" onde irá conter os registros do banco de dados
