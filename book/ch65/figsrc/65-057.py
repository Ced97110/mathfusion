import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(72)
# left : all permutations -> transitive ; right : {id, swap 1 2} -> not transitive
box(ax, 2, 14, 41, 50, 'sujet', fill=False)
box(ax, 45, 14, 41, 50, 'limite', fill=False)
text(ax, 22.5, 58, 'toutes les permutations', 'sujet', 's', weight='bold')
text(ax, 65.5, 58, 'identité et échange 1↔2', 'limite', 's', weight='bold')
def tri(cx, cy):
    return [(cx - 9, cy - 8), (cx + 9, cy - 8), (cx, cy + 8)]
L = tri(22.5, 38); R = tri(65.5, 38)
for P, role in ((L, 'sujet'), (R, 'limite')):
    for k, (x, y) in enumerate(P):
        pass
# nodes: 1 top, 2 bottom-left, 3 bottom-right
def nodes(cx, cy):
    return {1: (cx, cy + 8), 2: (cx - 10, cy - 8), 3: (cx + 10, cy - 8)}
NL = nodes(22.5, 36); NR = nodes(65.5, 36)
# left: arrows from 1 to 2 and 1 to 3
arrow(ax, (NL[1][0] - 2, NL[1][1] - 3.5), (NL[2][0] + 1.5, NL[2][1] + 4), 'varie', lw=1.1)
arrow(ax, (NL[1][0] + 2, NL[1][1] - 3.5), (NL[3][0] - 1.5, NL[3][1] + 4), 'varie', lw=1.1)
# right: swap 1<->2, 3 alone
arrow(ax, (NR[1][0] - 2, NR[1][1] - 3.5), (NR[2][0] + 1.5, NR[2][1] + 4), 'varie', lw=1.1, both=True)
for k in (1, 2, 3):
    disc(ax, NL[k][0], NL[k][1], 3.6, 'sujet', label='%d' % k)
for k in (1, 2):
    disc(ax, NR[k][0], NR[k][1], 3.6, 'sujet', label='%d' % k)
disc(ax, NR[3][0], NR[3][1], 3.6, 'limite', label='3')
text(ax, 22.5, 20, '1 atteint 2 et 3', 'sujet', 's')
text(ax, 65.5, 20, '3 ne bouge jamais', 'limite', 's')
text(ax, 22.5, 9, 'transitif', 'resultat', 'm', weight='bold')
text(ax, 65.5, 9, 'pas transitif', 'limite', 'm', weight='bold')
save(fig, '65-057')
