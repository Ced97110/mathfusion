import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def frac(ax, x, y, top, bot, rt, rb, w=11, size="m", dy=2.8):
    text(ax, x, y + dy, top, rt, size); text(ax, x, y - dy, bot, rb, size); line(ax, [(x - w / 2, y), (x + w / 2, y)], "encre", lw=0.8)
fig, ax = canvas(60)
y = 38
box(ax, 2, y - 5, 14, 10, 'sujet', label='5 j', size='m')
box(ax, 32, y - 5, 17, 10, 'autre', label='120 h', size='m')
box(ax, 64, y - 5, 22, 10, 'resultat', label='7 200 min', size='m', weight='bold')
arrow(ax, (16, y), (32, y), 'varie', lw=1.2)
frac(ax, 24, y + 8, '24 h', '1 j', 'autre', 'sujet', w=10, size='s', dy=2.4)
arrow(ax, (49, y), (64, y), 'varie', lw=1.2)
frac(ax, 56.5, y + 8, '60 min', '1 h', 'resultat', 'autre', w=11, size='s', dy=2.4)
arrow(ax, (9, y - 7), (75, y - 7), 'limite', curve=0.3)
text(ax, 44, 8, 'pas d’égalité directe j / min', 'limite', 's')
save(fig, '11-064')
