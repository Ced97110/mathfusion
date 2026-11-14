import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 6, 76, 'G : 8 éléments', 'sujet', 's', ha='left')
for i in range(8):
    box(ax, 6 + i * 10, 64, 9, 6, 'sujet')
for i in range(2):
    box(ax, 6 + i * 10, 52, 9, 6, 'varie')
text(ax, 28, 55, r'$\langle g\rangle$ : 2 éléments', 'varie', 's', ha='left')
for i in range(4):
    box(ax, 6 + i * 10, 40, 9, 6, 'autre')
text(ax, 50, 43, 'K : 8 ÷ 2 = 4 éléments', 'autre', 's', ha='left')
cx, cy = 24, 18
disc(ax, cx, cy, 8, 'fixe', fill=False, lw=0.6)
for dx, dy in ((8, 0), (0, 8), (-8, 0), (0, -8)):
    disc(ax, cx + dx, cy + dy, 1.8, 'autre')
text(ax, cx, 4, r'$K=\mathbb{Z}/4$', 'autre', 's')
text(ax, 44, 18, 'ou', 'fixe', 'm')
for dx in (-4, 4):
    for dy in (-4, 4):
        disc(ax, 64 + dx, cy + dy, 1.8, 'autre')
text(ax, 64, 4, r'$K=\mathbb{Z}/2\oplus\mathbb{Z}/2$', 'autre', 's')
arrow(ax, (20, 39), (24, 28), 'fixe')
arrow(ax, (38, 39), (62, 25), 'fixe')
save(fig, '60-256')
