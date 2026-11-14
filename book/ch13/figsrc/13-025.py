import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cs = (22, 44, 66); tx = ('3', r'$-$', '5'); rl = ('sujet', 'varie', 'sujet'); cap = ('départ', 'opération', 'à retirer')
for c, t, r, k in zip(cs, tx, rl, cap):
    box(ax, c - 8, 42, 16, 11, r, label=t, size='xl')
    text(ax, c, 38, k, r, 's')
y = 12
f = numberline(ax, 12, 64, y, -2, 3, labels=False)
text(ax, f(0), y - 4, '0', 'fixe', 's'); text(ax, f(3), y - 4, '3', 'sujet', 's')
disc(ax, f(3), y, 1.7, 'sujet'); disc(ax, f(-2), y, 1.7, 'resultat')
arrow(ax, (f(3), y + 2.5), (f(-2), y + 2.5), 'varie', curve=0.45)
text(ax, f(0.5), y + 17, 'retirer 5', 'varie', 's')
text(ax, f(-2), y - 5, '?', 'resultat', 'l', weight='bold')
save(fig, '13-025')
