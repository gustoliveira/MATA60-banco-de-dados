O projeto "Popular Database" é um sistema de gerenciamento de laboratório de informática que gera dados simulados para várias entidades, como estudantes, supervisores, computadores, armários e registros de acesso. Aqui está um resumo das principais funcionalidades:

## Estrutura do Projeto

O projeto está organizado em vários arquivos Python dentro do diretório `popular_database/models/`, cada um representando uma entidade ou funcionalidade específica:

- `advertencia.py`: Cria advertências com motivos aleatórios.
- `armario.py`: Gera armários com IDs únicos e localizações.
- `computador.py`: Cria um conjunto de computadores com diferentes status e tipos.
- `escala.py`: Gera uma escala completa para supervisores.
- `estudante.py`: Gera dados de estudantes, incluindo matrículas e e-mails.
- `registro_acesso.py`: Cria um registro completo de acesso ao laboratório.
- `registro_turno.py`: Registra os turnos dos supervisores.
- `supervisor.py`: Gera supervisores a partir do pool de estudantes.
- `utils.py`: Fornece funções utilitárias usadas em todo o projeto.

## Funcionalidades Principais

1. Geração de estudantes com dados aleatórios.
2. Criação de supervisores a partir dos estudantes.
3. Elaboração de uma escala completa para supervisores.
4. Geração de um registro detalhado de acesso ao laboratório.
5. Criação de computadores e armários com status variados.

## Como Executar

1. Instale as dependências necessárias:
   ```
   pip install faker
   ```

2. Execute o script principal:
   ```
   python main.py
   ```

O script `main.py` orquestra a criação de todas as entidades e imprime os dados gerados, incluindo listas de estudantes, supervisores, escala completa e registro de acesso ao laboratório.

Este projeto pode ser útil para testes, desenvolvimento ou como ponto de partida para popular um banco de dados de um sistema real de gerenciamento de laboratório de informática.

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/46844470/bec8f3e0-f3b8-4a1e-997f-a764815180e9/paste.txt

---
Resposta do Perplexity: pplx.ai/share
