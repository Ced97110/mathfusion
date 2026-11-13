import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
c, cy, k = 24, 34, 3.6
arrow(ax, (c - 16, cy), (c + 22, cy), 'fixe', lw=0.8); arrow(ax, (c, cy - 26), (c, cy + 26), 'fixe', lw=0.8)
z = (c + 3 * k, cy + 4 * k); zb = (c + 3 * k, cy - 4 * k)
line(ax, [z, zb], 'fixe', dash=True)
disc(ax, *z, 1.5, 'sujet'); disc(ax, *zb, 1.5, 'autre')
text(ax, z[0] + 2.5, z[1], r'$3+4i$', 'sujet', 's', ha='left'); text(ax, zb[0] + 2.5, zb[1], r'$3-4i$', 'autre', 's', ha='left')
text(ax, c + 20, cy + 3.5, 'réel', 'fixe', 's'); text(ax, c, 65, 'imaginaire', 'fixe', 's')
box(ax, 58, 18, 28, 32, 'resultat')
text(ax, 72, 42, r'$(3+4i)(3-4i)$', 'resultat', 's')
text(ax, 72, 34, r'$=25$', 'resultat', 'l')
text(ax, 72, 25, 'réel positif :', 'resultat', 's'); text(ax, 72, 21, 'rôle du carré', 'resultat', 's')
save(fig, '72-157')
