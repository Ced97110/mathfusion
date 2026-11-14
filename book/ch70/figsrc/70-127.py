import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
ox, oy, u = 26, 36, 15
X1 = ox + u
arrow(ax, (ox - 8, oy), (X1 + 36, oy), 'fixe', lw=0.7)
arrow(ax, (ox, oy - 22), (ox, oy + 26), 'fixe', lw=0.7)
text(ax, X1 + 38, oy - 3, r'$x$', 'fixe', 's')
text(ax, ox + 7, oy + 26, r'$y$ réel', 'fixe', 's')
line(ax, [(X1, oy - 22), (X1, oy + 24)], 'fixe', lw=0.6, dash=True)
for s, lab in ((1, r'$(1,\ i)$'), (-1, r'$(1,\ -i)$')):
    disc(ax, X1, oy + s * u, 1.5, 'sujet', fill=False, lw=1.0)
    text(ax, X1 + 4, oy + s * u, lab, 'sujet', 's', ha='left')
arrow(ax, (X1, oy + u - 2.5), (X1, oy + 2.5), 'varie', lw=0.9)
arrow(ax, (X1, oy - u + 2.5), (X1, oy - 2.5), 'varie', lw=0.9)
text(ax, X1 + 3, oy + 8, 'projeter', 'varie', 's', ha='left')
disc(ax, X1, oy, 1.3, 'resultat')
text(ax, X1, oy - 4.2, r'$x=1$', 'resultat', 's')
text(ax, X1 + 4, oy + 22, 'non réels', 'sujet', 's', ha='left')
text(ax, 44, 5, r'la projection perd « $y$ réel »', 'encre', 's')
save(fig, '70-127')
