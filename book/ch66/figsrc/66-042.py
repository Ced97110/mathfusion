import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
u = 10.0
x0 = 14.0
def panel(y, n, ds, lab):
    box(ax, x0, y + 14, n * u, 9, 'sujet', label=rf'$x^{n}-1$ : degré {n}')
    x = x0
    for d, g in ds:
        box(ax, x, y, g * u, 9, 'resultat', label=rf'$\Phi_{d}$')
        x += g * u
    text(ax, x0 + n * u / 2, y - 4.5, lab, 'resultat', 'm')
panel(48, 6, [(1, 1), (2, 1), (3, 2), (6, 2)], '1 + 1 + 2 + 2 = 6')
panel(10, 4, [(1, 1), (2, 1), (4, 2)], '1 + 1 + 2 = 4')
text(ax, 7, 70, r'$n=6$', 'sujet', 's')
text(ax, 7, 32, r'$n=4$', 'sujet', 's')
save(fig, '66-042')
