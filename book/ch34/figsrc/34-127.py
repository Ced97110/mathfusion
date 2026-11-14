import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
U = 35; y0 = 24
O1 = (3, y0); O2 = (47, y0)
poly(ax, [O1, (O1[0] + 0.8 * U, y0), (O1[0] + 0.8 * U, y0 + 0.6 * U)], 'sujet')
poly(ax, [O2, (O2[0] + 0.28 * U, y0), (O2[0] + 0.28 * U, y0 + 0.96 * U)], 'resultat')
text(ax, O1[0] + 7.5, y0 + 2.8, '$A$', 'sujet', 'm')
text(ax, O2[0] + 4.7, y0 + 2.8, '$2A$', 'resultat', 's')
text(ax, O1[0] + 0.4 * U, y0 - 3.2, '4/5', 'sujet', 's')
text(ax, O1[0] + 0.8 * U + 1.5, y0 + 0.3 * U, '3/5', 'sujet', 's', ha='left')
text(ax, O2[0] + 0.14 * U, y0 - 3.2, '7/25', 'resultat', 's')
text(ax, O2[0] + 0.28 * U + 1.5, y0 + 0.5 * U, '24/25', 'resultat', 's', ha='left')
text(ax, O1[0] + 0.3 * U - 1, y0 + 0.4 * U + 1, '1', 'fixe', 's')
text(ax, O2[0] + 0.0 * U + 0.5, y0 + 0.5 * U + 2, '1', 'fixe', 's')
arrow(ax, (O1[0] + 0.8 * U + 9, y0 + 0.9 * U), (O2[0] - 3, y0 + 0.9 * U), 'varie')
text(ax, 40, y0 + 0.9 * U + 3, r'$\times 2$', 'varie', 's')
for i, (t, x) in enumerate([(r'$\sin 2A$ = 24/25', 2), (r'$\cos 2A$ = 7/25', 31), (r'$\tan 2A$ = 24/7', 60)]):
    box(ax, x, 3, 26, 9, 'resultat', label=t, size='s')
save(fig, '34-127')
