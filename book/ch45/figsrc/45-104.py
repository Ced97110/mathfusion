import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
trees = [((('a','b'),'c'),'d'), (('a',('b','c')),'d'), (('a','b'),('c','d')), ('a',(('b','c'),'d')), ('a',('b',('c','d')))]
def depth(t): return 0 if isinstance(t, str) else 1 + max(depth(t[0]), depth(t[1]))
def draw(t, bx, ytop, dy, dx, cnt, role):
    if isinstance(t, str):
        i = cnt[0]; cnt[0] += 1; return bx + i * dx, ytop - 3 * dy
    (x1, y1), (x2, y2) = draw(t[0], bx, ytop, dy, dx, cnt, role), draw(t[1], bx, ytop, dy, dx, cnt, role)
    y = ytop - (3 - depth(t)) * dy; x = (x1 + x2) / 2
    line(ax, [(x1, y1), (x1, y), (x2, y), (x2, y2)], role, lw=1.1); return x, y
draw(trees[0], 30, 60, 6.5, 9, [0], 'sujet')
for i in range(4): disc(ax, 30 + i * 9, 60 - 19.5, 1.6, 'sujet')
text(ax, 18, 50, 'référence', 'sujet', 's', weight='bold'); text(ax, 18, 45.5, 'à gauche', 'sujet', 's')
for k in range(1, 5):
    bx = 6 + (k - 1) * 20; draw(trees[k], bx, 24, 4, 3.6, [0], 'fixe')
    for i in range(4): disc(ax, bx + i * 3.6, 12, 0.9, 'fixe')
    arrow(ax, (bx + 5.4, 26.5), (30 + 13.5 + (k - 2.5) * 5, 38), 'resultat')
text(ax, 44, 4, 'tous égaux à la référence', 'resultat', 's')
save(fig, '45-104')
