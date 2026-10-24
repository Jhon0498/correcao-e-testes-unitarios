# Correção e Testes Unitários em Python

## Sobre o projeto

Este projeto tem como objetivo corrigir erros em um programa Python que realiza o cadastro de alunos e o controle de suas notas, além de aplicar testes unitários para verificar se as funcionalidades estão funcionando corretamente.

O sistema permite cadastrar alunos, identificar a maior e a menor nota e validar se as notas estão dentro do intervalo permitido, de 0 a 10.

## Tecnologias utilizadas

- Python 3
- Biblioteca `unittest` para testes unitários
- Git e GitHub para controle de versão

## Estrutura do projeto

```text
semana-09-aula/
├── aluno.py       # Classe responsável pelos dados dos alunos
├── turma.py       # Cadastro de alunos e controle das notas
├── main.py        # Arquivo principal para executar o programa
├── testes.py      # Testes unitários do sistema
├── .gitignore     # Arquivos e pastas ignorados pelo Git
└── README.md      # Documentação do projeto
```

## Correções realizadas

- Correção da lógica de identificação da maior nota.
- Verificação da menor nota entre os alunos cadastrados.
- Validação das notas para aceitar somente valores entre 0 e 10.
- Desconsideração de alunos com notas fora do intervalo permitido.
- Implementação de testes unitários para verificar o comportamento do sistema.

## Testes unitários

Os testes foram desenvolvidos utilizando a biblioteca `unittest`, nativa do Python.

Foram criados seis testes para verificar:

1. Se a maior nota é identificada corretamente.
2. Se a menor nota é identificada corretamente.
3. Se as notas cadastradas respeitam o intervalo de 0 a 10.
4. Se as notas mínimas e máximas permitidas são aceitas.
5. Se uma turma sem alunos apresenta o comportamento esperado.
6. Se o sistema funciona corretamente quando os alunos possuem notas iguais.

## Como executar o projeto

É necessário ter o Python instalado.

No terminal, acesse a pasta do projeto e execute:

```bash
python main.py
```

## Como executar os testes

Na pasta do projeto, execute:

```bash
python -m unittest testes.py -v
```

O parâmetro `-v` exibe o resultado de cada teste individualmente.

Se todos os testes passarem, o resultado indicará que a execução foi concluída sem falhas.

## Objetivo do aprendizado

O projeto permite praticar a identificação e correção de erros, a criação de testes unitários e a verificação da lógica de um programa Python. Também demonstra como os testes ajudam a encontrar problemas antes que eles afetem o funcionamento do sistema.

## Autor

Jhonatan Mendes Morão
