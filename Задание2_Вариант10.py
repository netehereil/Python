import math

x = int(input("Введите x"))
y = int(input("Введите y"))
z = int(input("Введите z"))

s = (2 ** -x) * math.sqrt(x + 4 * (y ** (1/3))) * math.exp((x - 1) / math.sin(z))

print(f"Значение s: {s}")