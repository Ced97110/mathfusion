import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from bitkit import *
fig, ax = canvas(60)
tops, bots = ['1001', '1000', '0001'], ['0011001', '1110000', '1101001']
cx = [16, 44, 72]
for c, t, b in zip(cx, tops, bots):
    box(ax, c - 9, 42, 18, 9, 'sujet', label=rf'${t}$')
    box(ax, c - 12, 21, 24, 9, 'resultat', label=rf'${b}$')
    arrow(ax, (c, 41.5), (c, 31.5), 'varie', lw=1.2)
text(ax, 17.5, 36.5, 'coder', 'varie', 's', ha='left')
text(ax, 45.5, 36.5, 'coder', 'varie', 's', ha='left')
text(ax, 73.5, 36.5, 'coder', 'varie', 's', ha='left')
for y in (46.5, 25.5):
    text(ax, 30, y, '=', 'encre', 'l'); text(ax, 58, y, '+', 'encre', 'l')
box(ax, 14, 3, 60, 9, 'varie', label='le codage garde la somme')
crop(fig, ax, 0.0, 54.2)
save(fig, '68-134')
