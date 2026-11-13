import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
bw, bh = 18, 8
xs = [2, 22, 42]
text(ax, 31, 71, 'unités', 'fixe', 's'); text(ax, 75, 71, 'dixièmes', 'fixe', 's')
line(ax, [(62, 5), (62, 68)], 'fixe', dash=True)
# before
for i, x in enumerate(xs):
    box(ax, x, 54, bw, bh, 'varie' if i == 2 else 'sujet')
box(ax, 65, 54, 20, bh, 'fixe', fill=False, dash=True, label='vide', size='s')
text(ax, 31, 49, '3 baguettes', 'sujet', 's')
# cut
arrow(ax, (58, 52), (68, 36), 'varie')
text(ax, 38, 40, 'on coupe la 3e en 10', 'varie', 's')
# after
box(ax, 2, 22, bw, bh, 'sujet'); box(ax, 22, 22, bw, bh, 'sujet')
box(ax, 42, 22, bw, bh, 'fixe', fill=False, dash=True)
step = 20 / 10
for i in range(10):
    box(ax, 65 + i * step, 22, step, bh, 'varie' if i < 4 else 'fixe', r=0.1, lw=0.5)
text(ax, 21, 17, '2 baguettes', 'sujet', 's')
text(ax, 75, 17, '4 morceaux sur 10', 'varie', 's')
text(ax, 44, 7, 'la place de droite se remplit', 'encre', 's')
save(fig, '08-008')
