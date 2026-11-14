import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
ox, oy, u = 24, 46, 20
arrow(ax, (ox - 18, oy), (ox + 54, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 20), (ox, oy + 28), 'fixe', lw=0.8)
for p in ((ox + u, oy), (ox, oy + u)):
    ax.plot([p[0]], [p[1]], marker='o', ms=2, color=COL['fixe'], zorder=3)
arrow(ax, (ox, oy), (ox + u, oy), 'sujet', lw=1.6)
arrow(ax, (ox, oy), (ox, oy + u), 'varie', lw=1.6)
arrow(ax, (ox + u + 1, oy + 2), (ox + 2, oy + u - 1), 'varie', curve=0.35)
text(ax, ox + u + 4, oy - 4, r'$z=(1,0)$', 'sujet', 's', ha='left')
text(ax, ox + 3, oy + u + 7, r'$\lambda z=(0,1)$', 'varie', 's', ha='left')
text(ax, ox + 31, oy + 18, 'échange', 'varie', 's')
px, py = ox + 13, oy + 13
ax.plot([px, px], [oy, py], color=COL['resultat'], lw=0.8, ls='--', zorder=3)
ax.plot([ox, px], [py, py], color=COL['resultat'], lw=0.8, ls='--', zorder=3)
disc(ax, px, py, 1.5, 'resultat')
text(ax, px + 2, py + 3.5, r'$(a,b)$', 'resultat', 's', ha='left')
text(ax, 44, 20, r'$a\,z+b\,\lambda z=(a,b)$ : tout le plan', 'resultat', 's')
text(ax, 44, 9, r'ann $z$ = multiples de $\lambda^2-1$', 'sujet', 's')
save(fig, '60-161')
