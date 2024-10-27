# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

def f(x):
    return x ** 2

a = 0  
b = 2

# Monte Carlo method parameters
n_samples = 10000  # Number of random samples

x_random = np.random.uniform(a, b, n_samples)

y_random = f(x_random)

area_monte_carlo = (b - a) * np.mean(y_random)

area_quad, error_quad = spi.quad(f, a, b)

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Integration of f(x) = x^2 from ' + str(a) + ' to ' + str(b))

plt.grid()
plt.show()

print(f"Monte Carlo Integration: {area_monte_carlo}")
print(f"Analytical Integration: {area_quad}, Error: {error_quad}")
