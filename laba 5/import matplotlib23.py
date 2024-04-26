import matplotlib.pyplot as plt
import numpy as np

# Визначити функцію f(x)
def f(x, N, alpha):
  return N * (x / N + 0.5)**alpha - N / 2

# Створити масив значень x
x = np.arange(0, 1, 0.1)  # Крок 0.1 для точності

# Обчислити значення y
y = f(x, 9, 0.5)

# Намалювати графік
plt.plot(x, y, label='f(x) з кроком 0.1')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції f(x) на [0, 1]')
plt.grid(True)

# Протабулювання з кроком 0.01
print("x\ty (з кроком 0.1)")
for i in range(len(x)):
  print(f"{x[i]:.3f}\t{y[i]:.3f}")

# Протабулювання з кроком 0.1 (частина 1)
x_step01 = np.arange(0, 1, 0.1)
y_step01 = f(x_step01, 9, 0.5)
print("\nx\ty (з кроком 0.1 - частина 1)")
for i in range(len(x_step01)):
  print(f"{x_step01[i]:.3f}\t{y_step01[i]:.3f}")

# Порівняння результатів
print("\nПорівняння результатів:")
print("x (з кроком 0.1)\tx (з кроком 0.1)")
for i in range(len(x)):
  print(f"{x[i]:.3f}\t{x_step01[i]:.3f}")

# Відобразити графік
plt.legend()
plt.show()