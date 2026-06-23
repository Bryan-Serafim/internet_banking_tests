# language: pt
Funcionalidade: Regras de valor e saldo na transferência entre contas
  Como cliente do internet banking
  Quero que as transferências respeitem o saldo disponível e recusem valores inválidos
  Para que minha conta não seja debitada de forma indevida

  Contexto:
    Dado que a conta 1 possui saldo de 1000.00
    E que a conta 2 possui saldo de 500.00

  Cenario: Permitir transferência que zera exatamente o saldo de origem
    Quando a conta 2 transfere 500.00 para a conta 1
    Entao a transferência deve ser aceita
    E o saldo da conta 2 deve ficar em 0.00
    E o saldo da conta 1 deve ficar em 1500.00

  Cenario: Recusar transferência de valor zero
    Quando a conta 1 tenta transferir 0.00 para a conta 2
    Entao a transferência deve ser recusada por valor inválido
    E o saldo da conta 1 deve permanecer em 1000.00