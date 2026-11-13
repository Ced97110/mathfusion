import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

s = 20.0  # mm par unité
ox, oy = 8, 8
fig, ax = canvas(78)
r3 = math.sqrt(3)
z = (ox + r3 * s, oy + 1 * s)
w = (ox + 1 * s, oy + 1 * s)
zw = (ox + (r3 - 1) * s, oy + (r3 + 1) * s)
arrow(ax, (ox - 2, oy), (ox + 42, oy), 'fixe', lw=0.6)
arrow(ax, (ox, oy - 2), (ox, oy + 62), 'fixe', lw=0.6)
for p, role in [(z, 'sujet'), (w, 'autre'), (zw, 'resultat')]:
    line(ax, [(ox, oy), p], role, lw=1.1)
    disc(ax, p[0], p[1], 1.4, role)
for rad, a, role in [(9, 30, 'sujet'), (13, 45, 'autre'), (24, 75, 'resultat')]:
    ax.add_patch(Arc((ox, oy), 2 * rad, 2 * rad, theta1=0, theta2=a, ec=COL[role], lw=1.0, zorder=3))
text(ax, z[0] + 2.5, z[1] - 3, r'$z=\sqrt{3}+i$', 'sujet', 's', ha='left')
text(ax, w[0] - 2, w[1] + 3.5, r'$w=1+i$', 'autre', 's', ha='right')
text(ax, zw[0] - 2.5, zw[1] + 3.5, r'$zw$', 'resultat', 'm', ha='right')
text(ax, ox + 31, oy + 3.5, '30°', 'sujet', 's')
text(ax, ox + 17.5, oy + 3.5, '45°', 'autre', 's')
text(ax, ox + 22, oy + 12.5, '75°', 'resultat', 's')
box(ax, 48, 56, 38, 15, 'varie', label='forme algébrique\n' + r'$\approx 0{,}732+2{,}732\,i$', size='s')
box(ax, 48, 36, 38, 15, 'autre', label='forme polaire\n' + r'$2\sqrt{2}\ \mathrm{cis}\,75°$', size='s')
arrow(ax, (48, 63.5), (zw[0] + 2, zw[1] + 1), 'varie', lw=1.0)
arrow(ax, (48, 43.5), (zw[0] + 2, zw[1] - 1), 'autre', lw=1.0, curve=0.15)
text(ax, 67, 29, r'modules $2\times\sqrt{2}$', 'autre', 's')
text(ax, 67, 22.5, 'angles 30° + 45°', 'autre', 's')
text(ax, 67, 12, 'même point', 'resultat', 'm')
save(fig, '39-111')
