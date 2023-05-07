#  Voxel-TI Desafio Back End
Talvez eu esteja exagerando um pouco, já que isso é só um teste para estágio, mas eu quero mostrar como eu enxergo a solução de softwares no geral.

## Arquitetura Limpa
Apesar de eu estar usando arquitetura limpa aqui, com inversão de dependência e outras coisas, sendo uma aplicação pequena e de apenas demonstrações, não era realmente necessário. Mas uma aplicação tipica de web, que tem muitos paralelos com a realide e intrisicamente ligado com casos de usos, bem como escrever e pegar dados de um banco de dados, a arquitetura limpa se mostra muito eficiente na manutenção no longo prazo, e creio ser ideal para grande parte das aplicações web.

## Banco de dados
Utilizei o banco de dados sqlite3, popular principalmente para ambientes de testes e coisas assim, não muito adequado para software em produção, Dependendo da aplicação, poderia ser um noSQL como um mongoDB ou um dos SGBD sql já populares, como o mySQL e o postgreSQL, mas como é só um teste, decidi usar esse pela facilidade.

## Instruções
- pip install -r requirements.txt 
- Vá para a pasta root do projeto, onde há o arquivo "main.py"
- Execute python main.py

- baixa a extensão "SQLite Viewer" no visual studio code, para conseguir visualizar o banco de dados, ou busque a visualização de outra forma