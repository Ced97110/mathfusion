import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 68, 'les nombres de 0 à 12', 'fixe', 's')
rows = [(58, r'$\mathbb{Z}$ = (1)', 1, 'fixe'), (46, '(3)', 3, 'varie'),
        (34, '(6) pas maximal', 6, 'sujet'), (16, '(5) maximal', 5, 'resultat')]
for y, lab, step, role in rows:
    text(ax, 2, y, lab, role, 's', ha='left')
    for k in range(13):
        x = 36 + 4 * k
        if k % step == 0: disc(ax, x, y, 1.4, role)
        else: disc(ax, x, y, 0.35, 'fixe')
text(ax, 44, 7, r'rien entre $(5)$ et $\mathbb{Z}$', 'resultat', 's')
save(fig, '54-197')
