import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def col(cx, cy, pawn):
    h = 4.2
    pts = [(cx-h, cy-h), (cx+h, cy-h), (cx+h, cy+h), (cx-h, cy+h)]
    for i, (x, y) in enumerate(pts): disc(ax, x, y, 2.6, 'varie' if i == pawn else 'sujet')
col(12, 40, 3); col(40, 40, 0); col(72, 40, None)
arrow(ax, (20, 40), (32, 40), 'varie'); text(ax, 26, 46, r'$r$', 'varie', 's')
text(ax, 26, 60, 'même orbite', 'resultat', 's'); text(ax, 72, 60, 'autre orbite', 'limite', 's')
for x, n, r in ((12, 1, 'resultat'), (40, 1, 'resultat'), (72, 4, 'limite')):
    text(ax, x, 26, r'$|\mathrm{Stab}| = %d$' % n, r, 's')
text(ax, 26, 12, r'$1 = 1$', 'resultat', 'm'); text(ax, 72, 12, r'$4 \neq 1$', 'limite', 'm')
save(fig, '49-171')
