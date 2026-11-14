import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'$K$ : 4 éléments d’ordre $\leq2$', 'sujet', 'm')
for a in range(4):
    for b in range(2):
        role = 'varie' if (a, b) == (2, 0) else ('sujet' if a % 2 == 0 else 'fixe')
        box(ax, 14 + a * 16, 22 + b * 13, 15, 11.5, role, label=f'({a}, {b})')
text(ax, 18, 12, 'dans K', 'sujet', 's')
text(ax, 46, 12, 'g = (2, 0) est dans K', 'varie', 's')
text(ax, 77, 12, 'hors de K', 'fixe', 's')
save(fig, '60-258')
