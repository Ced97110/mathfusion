import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def fr(ax, cx, y, num, den, role, w=16, sz="m"):
    text(ax, cx, y + 4, num, role, sz); line(ax, [(cx - w / 2, y), (cx + w / 2, y)], role, lw=0.9); text(ax, cx, y - 4, den, role, sz)

fig, ax = canvas(64)
fr(ax, 18, 36, r'$\sqrt{3}$', r'$\sqrt{5}$', 'sujet')
box(ax, 10, 28, 16, 8, 'varie', fill=False, lw=1.2)
text(ax, 18, 17, 'bas irrationnel', 'varie', 's')
arrow(ax, (34, 38), (54, 38), 'varie')
text(ax, 44, 45, 'rationaliser', 'varie', 'm', weight='bold')
fr(ax, 72, 36, r'$\sqrt{15}$', r'$5$', 'resultat')
box(ax, 64, 28, 16, 8, 'resultat', fill=False, lw=1.2)
text(ax, 72, 17, 'bas rationnel', 'resultat', 's')
text(ax, 44, 6, 'même nombre, bas rendu rationnel', 'fixe', 's')
save(fig, '22-087')
