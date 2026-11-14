import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
cx = 44
def bx(w, y, h, role, label, lw=0.8, weight='normal'):
    box(ax, cx - w / 2, y, w, h, role, label=label, lw=lw, weight=weight)
bx(80, 86, 9, 'sujet', 'deux décompositions de M')
bx(70, 70, 9, 'fixe', 'réduction 1 : partie libre')
bx(60, 54, 9, 'fixe', 'réduction 2 : un premier')
bx(56, 32, 16, 'varie', 'réduction 3 : un seul premier\ncompare des dimensions', lw=1.8, weight='bold')
bx(60, 10, 9, 'resultat', 'mêmes annulateurs')
for ya, yb in ((86, 79.5), (70, 63.5), (54, 48.5), (32, 19.5)):
    arrow(ax, (cx, ya), (cx, yb), 'encre')
save(fig, '60-063')
