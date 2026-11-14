import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cx = [20, 44, 68]
for x, t, r in zip(cx, [r'$S$', r'$\times$', r'$T$'], ['sujet', 'varie', 'autre']):
    box(ax, x - 10, 60, 20, 14, r, label=t, size='l', weight='bold')
for x, t, r in zip(cx, ['1re place', 'croix', '2e place'], ['sujet', 'varie', 'autre']):
    arrow(ax, (x, 59), (x, 53), r); text(ax, x, 49, t, r, 'm')
arrow(ax, (44, 44), (44, 38), 'resultat')
for i in range(3):
    for j in range(2):
        disc(ax, 32 + 12 * i, 22 + 9 * j, 2.4, 'resultat')
text(ax, 44, 8, r'$S\times T$ : 6 couples', 'resultat', 'm')
save(fig, '42-163')
