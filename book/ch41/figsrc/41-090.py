import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
s = 3.6
# panneau gauche : deux vecteurs non nuls
ox, oy = 12, 40
P = lambda x, y: (ox + s * x, oy + s * y)
text(ax, 21, 70, 'deux vecteurs non nuls', 'resultat', 's')
arrow(ax, P(0, 0), P(4, 3), 'sujet', lw=1.5)
arrow(ax, P(0, 0), P(3, -4), 'autre', lw=1.5)
a1 = (0.8 * 3.5, 0.6 * 3.5); a2 = (0.6 * 3.5, -0.8 * 3.5)
line(ax, [(ox + a1[0], oy + a1[1]), (ox + a1[0] + a2[0], oy + a1[1] + a2[1]), (ox + a2[0], oy + a2[1])], 'resultat', lw=1.0)
text(ax, ox + 16, oy + 13.5, r'$u$', 'sujet', 'm')
text(ax, ox + 12, oy - 15, r'$v$', 'autre', 'm')
box(ax, 3, 6, 36, 9, 'resultat', label=r'$u\cdot v=0$ : $90^\circ$', size='s')
# panneau droit : u est le vecteur nul
ox2, oy2 = 56, 40
P2 = lambda x, y: (ox2 + s * x, oy2 + s * y)
text(ax, 66, 70, '$u$ = vecteur nul', 'limite', 's')
arrow(ax, P2(0, 0), P2(3, 4), 'autre', lw=1.5)
ax.plot([ox2], [oy2], marker='o', ms=4.5, color=COL['sujet'], zorder=6)
text(ax, ox2 - 4, oy2 - 4, r'$u$', 'sujet', 's')
text(ax, ox2 + 14, oy2 + 6, r'$v=\langle3,4\rangle$', 'autre', 's')
box(ax, 49, 6, 36, 9, 'limite', label=r'$u\cdot v=0$ : pas d’angle', size='s')
line(ax, [(44, 6), (44, 70)], 'fixe', lw=0.5, dash=True)
save(fig, '41-090')
