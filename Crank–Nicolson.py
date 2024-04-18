import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1.0  # Length of the domain
T = 1.0  # Total time
Nx = 100  # Number of spartial steps
Nt = 1000  # Number of time steps
dx = L / Nx  # Spartial step
dt = T / Nt  # Time step

# Initial condition
def initial_condition(x):
    return np.sin(np.pi * x)

# Function F : example of the heat equation
def F(u, x, t, du_dx, d2u_dx2):
    return d2u_dx2

# Initialize solution matrix
u = np.zeros((Nt+1, Nx+1))

# Set initial condition
x = np.linspace(0, L, Nx+1)
u[0, :] = initial_condition(x)

# Time iteration
for n in range(Nt):
    for i in range(1, Nx):
        du_dx = (u[n, i+1] - u[n, i-1]) / (2 * dx)
        d2u_dx2 = (u[n, i+1] - 2 * u[n, i] + u[n, i-1]) / dx**2
        u[n+1, i] = u[n, i] + dt * F(u[n, i], x[i], n*dt, du_dx, d2u_dx2)


# Plot the solution
plt.figure(figsize=(8, 6))
for n in range(0, Nt+1, int(Nt/10)):
    plt.plot(x, u[n, :], label=f"t = {n*dt:.2f}")
plt.xlabel('x')
plt.ylabel('u')
plt.title('Solution of PDE')
plt.legend()
plt.grid(True)
plt.show()