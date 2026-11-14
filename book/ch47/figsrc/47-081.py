import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
top = ['1', '¼ tour', '½ tour', '¾ tour']
bot = [r'$s\cdot$1', r'$s\cdot$¼', r'$s\cdot$½', r'$s\cdot$¾']
bw, g, x0 = 18.5, 2.0, 5.0
text(ax, 44, 65, r'4 rotations $H$ du carré', 'sujet', 'm')
text(ax, 44, 24, r'4 réflexions $sH$ du carré', 'autre', 'm')
for i in range(4):
    x = x0 + i * (bw + g)
    box(ax, x, 48, bw, 10, 'sujet', label=top[i], size='s')
    box(ax, x, 30, bw, 10, 'autre', label=bot[i], size='s')
    arrow(ax, (x + bw / 2, 48), (x + bw / 2, 40.5), 'varie')
    text(ax, x + bw / 2 + 1.5, 44.2, r'$s$', 'varie', 's', ha='left')
text(ax, 44, 11, '4 rotations, 4 réflexions : même taille', 'resultat', 's')
save(fig, '47-081')
