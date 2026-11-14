import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, '16 coloriages des 4 coins', 'encre', 's')
def sq(cx, cy, k):
    box(ax, cx - 6, cy - 6, 12, 12, 'fixe', lw=0.7, r=0.4)
    for m, (dx, dy) in enumerate(((-6, 6), (6, 6), (6, -6), (-6, -6))):
        disc(ax, cx + dx, cy + dy, 2.2, 'varie' if m == k else 'sujet')
cs = [(30, 50), (58, 50), (58, 26), (30, 26)]
box(ax, 14, 10, 60, 56, 'fixe', fill=False, dash=True, lw=0.7)
for k, (x, y) in enumerate(cs): sq(x, y, k)
arrow(ax, (38, 50), (50, 50), 'varie'); arrow(ax, (58, 42), (58, 34), 'varie')
arrow(ax, (50, 26), (38, 26), 'varie'); arrow(ax, (30, 34), (30, 42), 'varie')
text(ax, 44, 38, 'rotation', 'varie', 's')
text(ax, 44, 13, 'un paquet = un coloriage', 'resultat', 's')
text(ax, 44, 5, 'Burnside compte les paquets', 'resultat', 's')
save(fig, '74-183')
