import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(74)
text(ax, 44, 70, 'orbite = points atteints', 'fixe', 's')
# top: group {id, (1 2)} -> 2 orbits
text(ax, 3, 62, 'identité et échange 1↔2', 'limite', 's', ha='left', weight='bold')
box(ax, 4, 38, 40, 18, 'sujet', dash=True)
box(ax, 54, 38, 24, 18, 'autre', dash=True)
for x, v in ((16, 1), (32, 2)):
    disc(ax, x, 47, 4, 'sujet', label='%d' % v)
disc(ax, 66, 47, 4, 'autre', label='3')
arrow(ax, (20.5, 47), (27.5, 47), 'varie', lw=1.0, both=True)
text(ax, 24, 34, 'orbite {1, 2}', 'sujet', 's')
text(ax, 66, 34, 'orbite {3}', 'autre', 's')
text(ax, 44, 27, '2 orbites : pas transitif', 'limite', 's', weight='bold')
# bottom: transitive -> 1 orbit
text(ax, 3, 20, 'toutes les permutations', 'resultat', 's', ha='left', weight='bold')
box(ax, 4, 4, 60, 12, 'resultat', dash=True, fill=False)
for x, v in ((18, 1), (34, 2), (50, 3)):
    disc(ax, x, 10, 3.6, 'resultat', label='%d' % v)
text(ax, 76, 10, '1 orbite', 'resultat', 's', weight='bold')
save(fig, '65-058')
