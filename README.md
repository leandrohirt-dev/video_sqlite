# SQLite com Python - Exemplo Básico

Este é um projeto simples em Python que demonstra como conectar a um banco de dados SQLite, criar uma tabela de usuários e salvar as alterações. Ideal para iniciantes que estão aprendendo a integrar Python com SQLite.

## Funcionalidades

- Conexão e criação de um banco de dados SQLite (`meu_banco.db`).
- Criação de uma tabela de `usuarios` utilizando comandos SQL, garantindo que ela seja criada apenas se não existir.
- Fechamento seguro da conexão com o banco de dados.

## Pré-requisitos

- Python 3.x instalado em sua máquina.
- Como o `sqlite3` já é uma biblioteca embutida (built-in) no Python, não é necessário instalar nenhum pacote externo.

## Como Executar

1. Clone o repositório em sua máquina local:
   ```bash
   git clone https://github.com/leandrohirt-dev/video_sqlite.git
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd video_sqlite
   ```

3. Execute o script principal:
   ```bash
   python main.py
   ```

Após a execução, a mensagem `Banco de dados e tabela criados com sucesso!` será exibida e um arquivo chamado `meu_banco.db` será criado no diretório do projeto.

## Contribuição

Contribuições são sempre bem-vindas! Se você tiver alguma ideia para melhorar este exemplo, sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

## Licença

Este projeto é de código aberto e está disponível sob a [Licença MIT](LICENSE).
