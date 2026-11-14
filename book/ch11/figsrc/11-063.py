import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def frac(ax, x, y, top, bot, rt, rb, w=11, size="m", dy=2.8):
    text(ax, x, y + dy, top, rt, size); text(ax, x, y - dy, bot, rb, size); line(ax, [(x - w / 2, y), (x + w / 2, y)], "encre", lw=0.8)
fig, ax = canvas(64)
y = 46
text(ax, 6, y, '48', 'sujet', 'l'); text(ax, 13, y, 'h', 'sujet', 'l')
text(ax, 22, y, r'$\times$', 'encre', 'l')
text(ax, 34, y + 4, '1 j', 'resultat', 'l')
text(ax, 31, y - 4, '24', 'sujet', 'l'); text(ax, 37, y - 4, 'h', 'sujet', 'l')
line(ax, [(26, y), (42, y)], 'encre', lw=0.9)
text(ax, 49, y, '=', 'encre', 'l'); text(ax, 58, y, '2 j', 'resultat', 'l')
for sx, sy in ((13, y), (37, y - 4)):
    line(ax, [(sx - 2, sy - 2.6), (sx + 2, sy + 2.6)], 'varie', lw=1.4)
labs = [(9, '1 écrire', 'sujet', (9, y - 4)), (27, '2 multiplier', 'fixe', (33, y - 8)), (45, '3 barrer', 'varie', (37, y - 8)), (66, '4 calculer', 'fixe', (58, y - 4))]
for x, s, r, tgt in labs:
    text(ax, x, 26, s, r, 's')
    arrow(ax, (x, 29), (tgt[0], tgt[1] - 3.5 if False else tgt[1] - 4.2), 'fixe', lw=0.6)
box(ax, 6, 5, 76, 9, 'resultat', label='il ne reste que l’unité d’arrivée : stop', size='s')
save(fig, '11-063')
