### Descrição do Projeto:

Este app é o servidor da aplicação web construída para solucionar o desafio proposto pela e-rural.
O projeto foi construído utilizando a framework Flask do python 3.10.6. No projeto são definidos dois models:

- Room: representa uma sessão/sala
- Participant: representa um usuário/participante de uma sessão

São definidos ainda:

- Uma api REST para consulta e manipulação dos models.
- Websockets (utilizando flask-socket.io) para fornecer o serviço de sincronização de vídeo entre os participantes das sessões.

### Como Executar o App:

### 1 - Construindo e executando o container com o banco de dados PostgresSQl:

- Navegue até o diretório `db`
- Crie uma imagem a partir do dockerfile com o comando `docker build -t postgres-watch-party .`
- Execute o comando `docker run --name postgres-watch-party -p 5432:5432 -d postgres-watch-party
`, que irá executar o container e inicializar o database criando as enteidades necessárias.

### 2 - Executando o app Flask:

- Navegue até o diretório `app`
- instale as depêndencias utilizando `pip3 install -r requirements.txt`
- Execute o arquivo 'app.py': `python3 app.py`

### Testando a API e Websockets

Você pode realizar um teste simplificado das funcionalidades implementadas no projeto, através dos scripts disponibilizados.

#### Teste da API:

Para testar a api você pode executar o comando `python3 seed.py`, que populara as tabelas do postgres com alguns registros, a partir disto basta você acessar alguma rotas definidas em `app/api.py`.

(tente http://127.0.0.1:5000/watch/rooms - para listar todas as rooms)

#### Teste a sincronização com WebSockets:

Para testar a comunicação utilizando websockets, execute o comando `python3 websocket_clients.py` em **'app/test_scripts'** num terminal iterativo, ele fornecerá um menu simplificado que permitirá o envio e recebimento de mensagens. Rode o script em mais de um terminal, conecte dois participantes numa mesma sala e verifique que a comunicação entre eles e o servidor é sincronizada.

**Você pode ainda construir a interface web do app, e testar suas funcionalidades, seguindos as instruções contidas em [erural-watch-party-ui](https://github.com/Vitor-M/erural-watch-party-ui/)**
