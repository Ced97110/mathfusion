import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def B(ax, x, y, w, h, role, label, size='m', weight='normal'): return box(ax, x, y, w, h, role, label=label, size=size, weight=weight)
fig, ax = canvas(44)
text(ax, 20, 39, 'troisième lettre', 'varie', 's'); text(ax, 67, 39, 'inverse de', 'resultat', 's')
for i, (p, t, tail, r) in enumerate([('sé', 'c', 'ante', 'cos'), ('co', 's', 'écante', 'sin'), ('co', 't', 'angente', 'tan')]):
    y = 26 - i * 12
    B(ax, 4, y, 12, 9, 'fixe', p); B(ax, 16, y, 8, 9, 'varie', t, weight='bold')
    text(ax, 26, y + 4.5, tail, 'fixe', 'm', ha='left')
    arrow(ax, (42, y + 4.5), (58, y + 4.5), 'varie')
    B(ax, 58, y, 18, 9, 'resultat', r, weight='bold')
save(fig, '31-042')
