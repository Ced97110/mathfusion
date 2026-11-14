import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
ox, oy, s = 24, 12, 20.0
r = 2 ** 0.25
arrow(ax, (ox - 6, oy), (ox + 54, oy), 'fixe')
arrow(ax, (ox, oy - 4), (ox, oy + 42), 'fixe')
text(ax, ox + 54, oy - 4, 'axe réel', 'fixe', 's', ha='right')
text(ax, ox + 3, oy + 43, 'axe imaginaire', 'fixe', 's', ha='left')
disc(ax, ox + r * s, oy, 2.2, 'sujet')
text(ax, ox + r * s, oy + 6, r'$\sqrt[4]{2}$', 'sujet', 'm')
disc(ax, ox, oy + r * s, 2.2, 'autre')
text(ax, ox + 12, oy + r * s, r'$\sqrt[4]{2}\,i$', 'autre', 'm')
arrow(ax, (ox + r * s - 2.5, oy + 2.5), (ox + 2.5, oy + r * s - 2.5), 'varie', curve=-0.3, both=True)
text(ax, ox + 20, oy + 21, 'mêmes règles de calcul', 'varie', 's', ha='left')
text(ax, ox + 54, oy + 8, 'tous réels', 'sujet', 's', ha='right')
save(fig, '62-082')
