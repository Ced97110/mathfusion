import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
f = numberline(ax, 8, 68, 26, 0, 6, labels=False)
text(ax, 44, 56, 'nombres : des valeurs', 'fixe', 's')
for v, role in [(2, 'fixe'), (5, 'sujet')]:
    box(ax, f(v) - 8, 40, 16, 9, role, label=str(v), size='l')
    disc(ax, f(v), 26, 1.4, role if role == 'sujet' else 'fixe')
    arrow(ax, (f(v), 39.5), (f(v), 28), 'varie')
    text(ax, f(v), 18.5, f'graphe de {v}', role, 's')
arrow(ax, (f(2), 10), (f(5), 10), 'varie')
text(ax, (f(2) + f(5)) / 2, 5, 'à droite', 'varie', 's')
text(ax, 80, 32, 'points : des positions', 'fixe', 's', ha='right')
save(fig, '12-060')
