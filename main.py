# Leitura do tamanho da sequência
N = int(input())

# Leitura da sequência de números
sequencia = [int(input()) for _ in range(N)]

# Inicializando a contagem com 1 (para o primeiro número que é 1)
max_marked = 1

# Percorrer a sequência a partir do segundo número
for i in range(1, N):
    # Se o número atual é diferente do anterior, podemos marcar
    if sequencia[i] != sequencia[i - 1]:
        max_marked += 1

# Impressão do resultado
print(max_marked)
