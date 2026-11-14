import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cols = [(3, 18), (29, 18), (55, 30)]
top = [('7', 'sujet'), ('5', 'sujet'), ('12 → 0', 'resultat')]
bot = [('(3, 1)', 'autre'), ('(1, 2)', 'autre'), ('(4, 3) = (0, 0)', 'resultat')]
for (x, w), (t, r), (b, r2) in zip(cols, top, bot):
    box(ax, x, 42, w, 10, r, label=t, size='m')
    box(ax, x, 12, w, 10, r2, label=b, size='m')
    arrow(ax, (x + w / 2, 41.5), (x + w / 2, 22.5), 'varie')
for x in (25, 51):
    text(ax, x, 47, '+' if x == 25 else '=', 'encre', 'l'); text(ax, x, 17, '+' if x == 25 else '=', 'encre', 'l')
text(ax, 25.5, 32, 'placement', 'varie', 's')
save(fig, '60-021')
