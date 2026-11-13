import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def frac(ax, x, y, top, bot, rt, rb, w=11, size="m", dy=2.8):
    text(ax, x, y + dy, top, rt, size); text(ax, x, y - dy, bot, rb, size); line(ax, [(x - w / 2, y), (x + w / 2, y)], "encre", lw=0.8)
fig, ax = canvas(72)
text(ax, 44, 67, r'1 pied $=$ 12 po', 'sujet', 'l', weight='bold')
box(ax, 20, 55, 48, 5, 'sujet', label=None)
text(ax, 44, 57.5, 'pied', 'sujet', 's')
for i in range(12):
    box(ax, 20 + i * 4, 48, 4, 5, 'autre', r=0.2, lw=0.5)
text(ax, 44, 50.5, '12 po', 'autre', 's')
frac(ax, 20, 28, '1 pied', '12 po', 'sujet', 'autre', w=16, size='m')
text(ax, 20, 15, '= 1', 'resultat', 'm', weight='bold')
frac(ax, 68, 28, '12 po', '1 pied', 'autre', 'sujet', w=16, size='m')
text(ax, 68, 15, '= 1', 'resultat', 'm', weight='bold')
arrow(ax, (31, 28), (57, 28), 'varie', both=True)
text(ax, 44, 33, 'inverses', 'varie', 's')
save(fig, '11-055')
