import matplotlib.pyplot as plt
import numpy as np

# Визначити функцію f(x)
def f(x, N, alpha):
  return N * (x / N + 0.5)**alpha - N / 2

# Створити масив значень x
x = np.arange(0, 1, 0.01)

# Обчислити значення y
y = f(x, 11, 0.5)

# Намалювати графік
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції f(x) на [0, 1]')
plt.grid(True)

# Протабулювання
print("x\ty")
for i in range(len(x)):
  print(f"{x[i]:.3f}\t{y[i]:.3f}")

# Відобразити графік
plt.show()