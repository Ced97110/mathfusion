import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 4.0
def grid(x0, n, r):
    for i in range(n):
        for j in range(n):
            box(ax, x0 + i * u, 22 + j * u, u, u, r, label=None, r=0.15, lw=0.5)
grid(10, 4, 'sujet'); grid(48, 5, 'autre')
text(ax, 10 + 2 * u, 22 + 4 * u + 3.5, 'côté 4', 'sujet', 's')
text(ax, 48 + 2.5 * u, 22 + 5 * u + 3.5, 'côté 5', 'autre', 's')
text(ax, 10 + 2 * u, 17.5, r'$4^2 = 16$', 'sujet', 'm')
text(ax, 48 + 2.5 * u, 17.5, r'$5^2 = 25$', 'autre', 'm')
text(ax, 10 + 2 * u, 5, '4 : racine carrée de 16', 'sujet', 's')
text(ax, 48 + 2.5 * u, 3, '5 : racine carrée de 25', 'autre', 's')
save(fig, '22-024')
