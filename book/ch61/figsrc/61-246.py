import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 22, 65, 'tour quadratique', 'sujet', 's'); text(ax, 66, 65, 'tour de radicaux', 'autre', 's')
for x, r, l in [(4, 'sujet', r'$u_i^2$'), (48, 'autre', r'$u_i^{n}$')]:
    for k, y in enumerate([18, 33, 48]):
        box(ax, x, y, 18, 9, r, label=[r'$F$', r'$F(u_1)$', r'$F(u_2)$'][k])
        if k < 2: arrow(ax, (x + 9, y + 9.5), (x + 9, y + 14.5), 'varie')
    text(ax, x + 28, 35.5, l, 'varie', 'm')
text(ax, 22, 8, r'$\sqrt[3]{2}$ n’entre jamais', 'limite', 's')
text(ax, 66, 8, r'$\sqrt[3]{2}$ est accepté', 'resultat', 's')
save(fig, '61-246')
