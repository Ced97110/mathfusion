import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

cx, cy, k = 50, 42, 14.0
fig, ax = canvas(84)
arrow(ax, (4, cy), (86, cy), 'fixe', lw=0.7)
arrow(ax, (cx, 6), (cx, 76), 'fixe', lw=0.7)
r3 = math.sqrt(3)
# cas D < 0 : -1 ± √3 i
ptop = (cx - k, cy + r3 * k); pbot = (cx - k, cy - r3 * k)
line(ax, [ptop, pbot], 'sujet', lw=0.8, dash=True)
line(ax, [(cx - k, cy - 1.2), (cx - k, cy + 1.2)], 'sujet', lw=1.2)
disc(ax, ptop[0], ptop[1], 1.5, 'sujet'); disc(ax, pbot[0], pbot[1], 1.5, 'sujet')
text(ax, ptop[0] - 2.5, ptop[1] + 3, r'$-1+\sqrt{3}\,i$', 'sujet', 's', ha='right')
text(ax, pbot[0] - 2.5, pbot[1] - 3, r'$-1-\sqrt{3}\,i$', 'sujet', 's', ha='right')
text(ax, 4, 80, r'$x^2+2x+4=0$ : $D=-12<0$', 'sujet', 's', ha='left')
text(ax, cx + 4, cy - 3, 'axe horizontal', 'fixe', 's', ha='left')
text(ax, cx - k - 2, cy + 3.5, '−1', 'fixe', 's', ha='right')
# contre-exemple : x^2 - 4 = 0, D = 16
disc(ax, cx + 2 * k, cy, 1.5, 'limite'); disc(ax, cx - 2 * k, cy, 1.5, 'limite')
text(ax, cx + 2 * k, cy + 4, '2', 'limite', 's')
text(ax, cx - 2 * k, cy + 4, '−2', 'limite', 's')
text(ax, 84, 24, r'$x^2-4=0$ : $D=16>0$', 'limite', 's', ha='right')
text(ax, 84, 17, 'solutions sur l’axe,', 'limite', 's', ha='right')
text(ax, 84, 10.5, 'pas de part et d’autre', 'limite', 's', ha='right')
save(fig, '39-120')
