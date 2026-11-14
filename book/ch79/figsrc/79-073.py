import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
d4, d6, d12, d60 = (10, 12), (34, 12), (22, 40), (22, 68)
box(ax, 1, 4, 42, 17, 'sujet', fill=False, dash=True)
box(ax, 13, 31, 18, 46, 'varie', fill=False, dash=True)
import math
def cut(a, b, r=4.2):
    d = math.hypot(b[0]-a[0], b[1]-a[1]); u = ((b[0]-a[0])/d, (b[1]-a[1])/d)
    return [(a[0]+u[0]*r, a[1]+u[1]*r), (b[0]-u[0]*r, b[1]-u[1]*r)]
for a, b in [(d4, d12), (d6, d12), (d12, d60)]:
    line(ax, cut(a, b), 'fixe')
disc(ax, *d4, 4.2, 'sujet', label='4'); disc(ax, *d6, 4.2, 'sujet', label='6')
disc(ax, *d12, 4.2, 'resultat', label='12'); disc(ax, *d60, 4.2, 'varie', label='60')
text(ax, 22, 6.5, r'$A$', 'sujet', 'm')
text(ax, 38, 68, r'$B$', 'varie', 'm'); text(ax, 38, 40, r'$b$', 'resultat', 'm')
BX, BW = 46, 40
box(ax, BX, 4, BW, 12, 'sujet', label=r'$A = \{4, 6\}$', size='s')
box(ax, BX, 24, BW, 12, 'varie', label='$B$ : les majorants de $A$', size='s')
box(ax, BX, 44, BW, 12, 'varie', label='$b$ : plus grand minorant\nde $B$, donc $b = 12$', size='s', weight='bold')
box(ax, BX, 64, BW, 12, 'resultat', label=r'$b = \sup A = 12$', size='s')
for y in (16, 36, 56): arrow(ax, (BX + BW / 2, y), (BX + BW / 2, y + 8), 'fixe')
save(fig, '79-073')
