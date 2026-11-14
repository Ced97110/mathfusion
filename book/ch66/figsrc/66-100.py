import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for i in range(8):
    n = i + 1
    ok = n in (1, 2, 4, 8)
    box(ax, 3 + 10.2 * i, 26, 9.6, 10, 'resultat' if ok else 'limite', label=str(n), size='l', lw=1.8 if n == 3 else 0.8)
box(ax, 4, 46, 36, 10, 'sujet', label='∛2 : degré 3', size='m')
box(ax, 46, 46, 38, 10, 'autre', label='cos 20° : degré 3', size='m')
x3 = 3 + 10.2 * 2 + 4.8
arrow(ax, (24, 45.5), (x3 - 1.5, 37.5), 'sujet')
arrow(ax, (54, 45.5), (x3 + 1.5, 37.5), 'autre')
poly(ax, [(4, 11), (8, 11), (8, 15), (4, 15)], 'resultat')
text(ax, 10, 13, 'puissance de 2', 'resultat', 's', ha='left')
poly(ax, [(46, 11), (50, 11), (50, 15), (46, 15)], 'limite')
text(ax, 52, 13, 'pas une puissance de 2', 'limite', 's', ha='left')
save(fig, '66-100')
