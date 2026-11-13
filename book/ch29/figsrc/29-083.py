import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 4
def grid(x0, y0, n, role):
    for i in range(n):
        for j in range(n):
            poly(ax, [(x0 + i * u, y0 + j * u), (x0 + (i + 1) * u, y0 + j * u), (x0 + (i + 1) * u, y0 + (j + 1) * u), (x0 + i * u, y0 + (j + 1) * u)], role, lw=0.4)
grid(8, 14, 3, 'sujet')
grid(42, 14, 6, 'sujet')
text(ax, 14, 30, 'r = 3', 'sujet', 'm')
text(ax, 54, 42, 'r = 6', 'sujet', 'm')
text(ax, 14, 8, '3 × 3 = 9', 'sujet', 'm')
text(ax, 54, 8, '6 × 6 = 36', 'sujet', 'm')
arrow(ax, (22, 22), (40, 22), 'varie')
text(ax, 31, 26.5, 'r doublé', 'varie', 's')
text(ax, 31, 17.5, 'carré × 4', 'varie', 's')
save(fig, '29-083')
