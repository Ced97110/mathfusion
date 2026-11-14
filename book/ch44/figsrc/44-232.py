import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
def pg(cx, cy, R, n, rot=90): return [pol(cx, cy, R, rot + 360 * k / n) for k in range(n)]
fig, ax = canvas(62)
p, s = 3.1, 2.6
def row(y, n, role, extra=0):
    for i in range(n): box(ax, 2 + i * p, y, s, s, role, r=0.3, lw=0.5)
    for i in range(extra): box(ax, 2 + (n + i) * p, y, s, s, 'limite', r=0.3, lw=0.5)
text(ax, 2, 57, '3 côtés : 6 mouvements', 'sujet', 's', ha='left'); row(51, 6, 'sujet')
text(ax, 2, 45, '6 permutations de 1, 2, 3', 'autre', 's', ha='left'); row(39, 6, 'autre')
text(ax, 44, 45, r'$D_3 = S_3$', 'resultat', 'l')
text(ax, 2, 31, '4 côtés : 8 mouvements', 'sujet', 's', ha='left'); row(25, 8, 'sujet')
text(ax, 2, 19, '24 permutations de 1, 2, 3, 4', 'autre', 's', ha='left'); row(13, 8, 'autre', 16)
text(ax, 2, 7, '16 ne sont pas des mouvements', 'limite', 's', ha='left')
text(ax, 70, 31, r'$D_4 < S_4$', 'limite', 'l')
save(fig, '44-232')
