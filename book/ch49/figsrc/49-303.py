import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, '10 points ; groupe de 9 éléments', 'sujet', 's')
xs = [6 + i * 8 for i in range(10)]
for i, x in enumerate(xs):
    fixed = i == 9
    disc(ax, x + 2, 48, 3.0, 'resultat' if fixed else 'fixe')
for g in range(3):
    x0 = xs[g * 3] - 1.5; x1 = xs[g * 3 + 2] + 5.5
    box(ax, x0, 42, x1 - x0, 12, 'fixe', fill=False, dash=True, r=1.0)
text(ax, 34, 60, 'paquets de 3 (ou 9)', 'fixe', 's')
text(ax, xs[9] + 2, 60, 'reste', 'resultat', 's')
brace(ax, xs[0] - 1.5, xs[8] + 5.5, 40, 'fixe', label='multiples de 3')
brace(ax, xs[9] - 1.5, xs[9] + 5.5, 40, 'resultat', label='1', depth=1.6)
box(ax, 8, 6, 72, 12, 'resultat')
text(ax, 44, 12, r'$10 = 3 \times 3 + 1$ : un point fixe', 'resultat', 's')
save(fig, '49-303')
