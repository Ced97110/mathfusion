import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, r'orbite de $P_A$ sous $P_A$', 'sujet', 'm')
for y, s, role, lab, res, rl in ((36, r'par $s_A\in P_A$', 'sujet', r'$P_A$', 'fixé', 'resultat'),
                                 (12, r'par $s_B\notin P_A$', 'autre', r'$P_C$', 'déplacé', 'limite')):
    disc(ax, 12, y, 4.6, 'sujet', label=r'$P_A$', size='s')
    arrow(ax, (17.5, y), (55, y), 'varie'); text(ax, 36, y + 4.5, 'conjugué ' + s, 'varie', 's')
    disc(ax, 61, y, 4.6, role, label=lab, size='s'); text(ax, 77, y, res, rl, 's')
save(fig, '50-098')
