import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, 'tailles possibles d’un sous-groupe de 12', 'fixe', 's')
for n in range(1, 13):
    role = 'limite' if n in (5, 7, 8, 9, 10, 11) else 'resultat' if n in (2, 3, 4) else 'fixe'
    box(ax, 1.5 + (n - 1) * 7.15, 41, 6.4, 9, role, label=str(n), size='s', dash=role == 'fixe')
for y, role, s_ in [(30, 'limite', 'ne divise pas 12 : interdit (Lagrange)'),
                    (21, 'resultat', 'puissance d’un premier : garanti (Sylow)'),
                    (12, 'fixe', 'ni l’un ni l’autre : ouvert')]:
    box(ax, 6, y - 2.5, 5, 5, role, r=0.3, dash=role == 'fixe')
    text(ax, 14, y, s_, role, 's', ha='left')
save(fig, '47-095')
