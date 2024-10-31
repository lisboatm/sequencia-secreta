# README - Sequência de Números no Palácio Imperial

## Descrição do Problema

Na calçada em frente ao Palácio Imperial, existe uma sequência de números que começa e termina com o número 1, contendo apenas os números 1 e 2. O número 2 deve aparecer pelo menos uma vez na sequência. O desafio consiste em determinar a quantidade máxima de números da sequência que podem ser marcados com um círculo, garantindo que não haja dois números iguais consecutivos na sequência marcada.

### Exemplo de Sequência

A sequência pode se parecer com a seguinte:

```
1
2
1
1
2
2
1
```

- No exemplo acima, a sequência começa e termina com o número 1 e contém o número 2.

## Objetivo

O objetivo é escrever um programa que calcule e imprima a quantidade máxima de números da sequência que podem ser marcados, respeitando a condição de que números iguais não podem ser consecutivos.

## Entrada

- A primeira linha contém um inteiro \( N \) representando o tamanho da sequência (3 ≤ \( N \) ≤ 500).
- As \( N \) linhas seguintes contêm, cada uma, um inteiro \( V_i \) (1 ≤ \( i \) ≤ \( N \)), que define a sequência de números desenhados no chão, onde \( V_i \) é igual a 1 ou 2.

### Exemplo de Entrada

```
7
1
2
1
1
2
2
1
```

## Saída

- O programa deve imprimir uma única linha contendo um número inteiro que representa a quantidade máxima de números da sequência que podem ser marcados sem que haja dois números iguais consecutivos.

### Exemplo de Saída

Para a entrada acima, a saída seria:

```
5
```

## Restrições

- A sequência sempre começa e termina com o número 1.
- O número 2 deve aparecer pelo menos uma vez na sequência.
- A sequência deve conter apenas os números 1 e 2.

## Solução

Para resolver o problema, siga os seguintes passos:

1. **Leitura dos Dados**: Capture o tamanho da sequência e os números que a compõem.
2. **Cálculo da Quantidade Máxima**: Percorra a sequência e conte quantos números podem ser marcados, garantindo que não haja números iguais consecutivos.
3. **Impressão do Resultado**: Exiba o resultado da contagem.

## Exemplo de Implementação

```python
# Leitura do tamanho da sequência
N = int(input())

# Leitura da sequência
sequencia = [int(input()) for _ in range(N)]

# Inicialização da contagem
max_count = 1  # Começamos contando o primeiro número

# Percorre a sequência para contar a quantidade máxima
for i in range(1, N):
    if sequencia[i] != sequencia[i - 1]:  # Se o número atual for diferente do anterior
        max_count += 1  # Incrementa a contagem

# Impressão do resultado
print(max_count)
```

## Conclusão

Esse programa permite que você determine a quantidade máxima de números que podem ser marcados na sequência, respeitando as restrições impostas. Divirta-se programando!
