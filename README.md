# Projeto de Conectividade IoT

Este projeto oferece uma estrutura para interação com dispositivos IoT através de uma conexão estabelecida.

## Funcionalidades

- Estabelecimento de conexão com dispositivos IoT.
- Envio de mensagens para os dispositivos conectados.
- Recebimento de mensagens dos dispositivos conectados.

## Classes Principais

### `Connection`

A classe `Connection` gerencia a conexão com os dispositivos. Principais métodos incluem:

- `connect(nome: str, ip: str, porta: int) -> None`: Conecta-se a um dispositivo através do nome, IP e porta especificados.
- `disconnect() -> None`: Desconecta-se do dispositivo atualmente conectado.
- `send(mensagem: Union[str, Enum]) -> None`: Envia uma mensagem para o dispositivo conectado.
- `receive() -> str`: Recebe uma mensagem do dispositivo conectado.

### `IOTDevice`

A classe `IOTDevice` representa um dispositivo IoT genérico. Principais métodos incluem:

- `connect(nome: str, ip: str, porta: int) -> None`: Conecta-se a um dispositivo utilizando a conexão fornecida.
- `disconnect() -> None`: Desconecta-se do dispositivo atual.
- `send(mensagem: Union[str, Enum]) -> None`: Envia uma mensagem para o dispositivo conectado.
- `receive() -> str`: Recebe uma mensagem do dispositivo conectado.

### Mensagens

- `LightMessage`: Enumeração das mensagens para dispositivos de iluminação.
- `MotionMessage`: Enumeração das mensagens para sensores de movimento.

## Uso Exemplo

```python
# Exemplo de uso do código
# ...

# Conectando-se a um dispositivo
connection.connect('user', '192.168.1.1')

# Interagindo com um dispositivo de iluminação
light = Light(connection)
light.send(LightMessage.TURN_ON)

# Interagindo com um sensor de movimento
motion_sensor = MotionSensor(connection)
motion_sensor.send(MotionMessage.MOTION_DETECTED)

# Desconectando do dispositivo
connection.disconnect()
```

## Melhorias Recentes

As melhorias recentes feitas no código incluem:

- Adição de dicas de tipo para parâmetros de função e valores de retorno para melhorar a legibilidade e a manutenção.
- Utilização de f-strings para melhorar a legibilidade e formatação de strings no código.
- Validação do formato do endereço IP usando regex para maior robustez na verificação.
- Substituição de strings por enums para tipos de mensagens, evitando erros de valores inválidos.
- Adição de docstrings para documentação de métodos e classes, facilitando a compreensão e a manutenção do código.

Essas melhorias têm como objetivo aprimorar a estrutura, a legibilidade e a confiabilidade do código, seguindo boas práticas de desenvolvimento.


## Requisitos

- Python 3.x
- Bibliotecas usadas:
  - `abc`: Módulo Python para a definição de classes abstratas.
  - `enum`: Módulo Python para criação de enumerações.
  - `logging`: Módulo Python para geração de logs.
  - `re`: Módulo Python para operações com expressões regulares (regex).
  - `typing`: Módulo Python para suporte a tipos.


## Contribuição
Sinta-se à vontade para contribuir com sugestões, melhorias ou reportar problemas abrindo uma issue ou submetendo um pull request.

## Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
