import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def fr(ax, cx, y, num, den, role, w=16, sz="m"):
    text(ax, cx, y + 4, num, role, sz); line(ax, [(cx - w / 2, y), (cx + w / 2, y)], role, lw=0.9); text(ax, cx, y - 4, den, role, sz)

fig, ax = canvas(70)
fr(ax, 14, 52, r'$3$', r'$4+\sqrt{6}$', 'sujet', w=20, sz='s')
text(ax, 31, 52, r'$\times$', 'encre', 'xl')
fr(ax, 48, 52, r'$4-\sqrt{6}$', r'$4-\sqrt{6}$', 'varie', w=20, sz='s')
text(ax, 65, 52, '=', 'encre', 'xl')
fr(ax, 77, 52, r'$12-3\sqrt{6}$', r'$10$', 'resultat', w=18, sz='s')
box(ax, 2, 22, 40, 9, 'resultat', label=r'bas : $16-6=10$', size='s')
box(ax, 46, 22, 40, 9, 'sujet', label=r'haut : $3(4-\sqrt{6})$', size='s')
text(ax, 44, 11, 'des deux côtés : environ 0,465', 'fixe', 's')
save(fig, '22-091')
