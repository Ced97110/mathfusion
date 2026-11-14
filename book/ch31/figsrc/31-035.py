import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def B(ax, x, y, w, h, role, label, size='m', weight='normal'): return box(ax, x, y, w, h, role, label=label, size=size, weight=weight)
fig, ax = canvas(56)
text(ax, 17, 52, 'angle 35°', 'sujet', 's'); text(ax, 71, 52, 'angle complémentaire 55°', 'autre', 's')
rows = [('cos 35°', 'sin 55°', '0,8192'), ('cotan 35°', 'tan 55°', '1,4281'), ('cosec 35°', 'sec 55°', '1,7434')]
for i, (a, b, v) in enumerate(rows):
    y = 34 - i * 15
    B(ax, 4, y, 26, 10, 'sujet', a); B(ax, 58, y, 26, 10, 'autre', b)
    line(ax, [(30, y + 5), (36, y + 5)], 'resultat', lw=1.2); line(ax, [(52, y + 5), (58, y + 5)], 'resultat', lw=1.2)
    text(ax, 44, y + 5, v, 'resultat', 'm', weight='bold')
save(fig, '31-035')
