# Løsning av Partielle Differensiallikninger numerisk
Dette Python-skriptet demonstrerer hvordan man kan løse en partiell differensiallikning (PDE) numerisk ved hjelp av endelig differansemetode. Vi bruker varmeledningslikningen som et eksempel for å illustrere metoden.

## Kodeforklaring
Parametere
L: Lengden på domenet
T: Total tid
Nx: Antall romlige steg
Nt: Antall tidssteg
dx: Romlig steglengde
dt: Tidssteglengde

## Initialbetingelse
Vi definerer initialbetingelsen for PDEen ved å bruke en sinusfunksjon:
<pre>

def initialbetingelse(x):
    return np.sin(np.pi * x)
</pre>

## Funksjon F
For dette eksempelet bruker vi varmeledningslikningen, og funksjonen F er definert som:

<pre>
def F(u, x, t, du_dx, d2u_dx2):
    return d2u_dx2
</pre>

## Tidsiterasjon
Vi itererer over tid for å beregne løsningen ved hvert tidssteg ved hjelp av endelig differansemetode:

<pre>
for n in range(Nt):
    for i in range(1, Nx):
        du_dx = (u[n, i+1] - u[n, i-1]) / (2 * dx)
        d2u_dx2 = (u[n, i+1] - 2 * u[n, i] + u[n, i-1]) / dx**2
        u[n+1, i] = u[n, i] + dt * F(u[n, i], x[i], n*dt, du_dx, d2u_dx2)
</pre>

## Plotting
Til slutt plotter vi løsningen ved ulike tidssteg ved hjelp av Matplotlib:
<pre>
plt.figure(figsize=(8, 6))
for n in range(0, Nt+1, int(Nt/10)):
    plt.plot(x, u[n, :], label=f"t = {n*dt:.2f}")
plt.xlabel('x')
plt.ylabel('u')
plt.title('Løsning av PDE')
plt.legend()
plt.grid(True)
plt.show()
</pre>
