# Exemplo de uso de fila (deque)
# Serve para entender a ideia de "primeiro que entra, primeiro que sai" (FIFO).

from collections import deque

fila = deque()
fila.append("A")
fila.append("B")
fila.append("C")

print("Fila inicial:", list(fila))

print("Saiu:", fila.popleft())  # A
print("Fila agora:", list(fila))

print("Saiu:", fila.popleft())  # B
print("Fila agora:", list(fila))
